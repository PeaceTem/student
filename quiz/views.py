
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# function based views
from .forms import NewQuizForm, NewQuestionForm, NewAnswerForm

from django.views.generic.list import ListView

from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from .models import Quizzes, Answer, Question, Attempter, Attempt


# the quiz list view
@login_required(login_url='login')
def QuizList(request):
    user = request.user
    quizzes = Quizzes.objects.all()

    # if request.method == 'POST':
        # if form.is_valid():
    search_input= request.GET.get('search-area') or ''
    print(search_input)
    if search_input:
        quizzes = Quizzes.objects.filter(title__icontains=search_input)

        context={
            'quizzes': quizzes,
            'search_input': search_input,
        }
        return render(request, 'quiz/quizzes_list.html', context)

    context={
        'quizzes': quizzes,
    }
    return render(request, 'quiz/quizzes_list.html', context)






# create a new quiz
@login_required(login_url='login')
def NewQuiz(request):
    user = request.user
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            description=form.cleaned_data.get('description')
            quiz = Quizzes.objects.create(user=user, title=title, description=description)
            return redirect('quiz:new-question', quiz_id=quiz.id)

    else:
        form = NewQuizForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/newquiz.html', context)



# create an update quiz view
@login_required(login_url='login')
def UpdateQuiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    # quiz = Quizzes.objects.get(id=quiz_id)
    form = NewQuizForm(instance=quiz)

    if request.method == 'POST':
        form = NewQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('quiz:quiz-detail', quiz_id=quiz.id)

    context = {
        'form': form,
    }

    return render(request, 'quiz/newquiz.html', context)



# create the quiz delete view
@login_required(login_url='login')
def DeleteQuiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz:quizzes')
    
    return render(request, 'quiz/quiz_delete.html', {'obj': quiz})

# create a new question
@login_required(login_url='login')
def NewQuestion(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)

    if user != quiz.user:
        return HttpResponseForbidden
    
    if request.method=='POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data.get('question_text')
            points = form.cleaned_data.get('points')
            answer_text = request.POST.getlist('answer_text')
            is_correct = request.POST.getlist('is_correct')
            question = Question.objects.create(question_text=question_text, user=user, points=points)
           
            for a, c in zip(answer_text, is_correct):

                answer = Answer.objects.create(answer_text=a, is_correct=(c == 'True'), user=user)
                question.answers.add(answer)
                question.save()
                quiz.questions.add(question)
                quiz.save()
            return redirect('quiz:new-question', quiz_id=quiz.id)

    else:
        form = NewQuestionForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'quiz/newquestion.html', context)




# the details of a quiz
def QuizDetail(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    my_attempts = Attempter.objects.filter(quiz=quiz, user=user)
    
    context = {
        'quiz': quiz,
        'my_attempts': my_attempts,
        'user': user,
    }
    return render(request, 'quiz/quizdetail.html', context)



# the real test view
def TakeQuiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)

    context = {
        'quiz': quiz,
    }
    return render(request, 'quiz/takequiz.html', context)



# the result view
def SubmitAttempt(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    total_score = 0

    if request.method == 'POST':
        questions = request.POST.getlist('question')
        answers = request.POST.getlist('answer')
        attempter = Attempter.objects.create(user=user, quiz=quiz, score=0)
        attempts = []
        
        for q, a in zip(questions, answers):
            question = Question.objects.get(id=q)
            answer = Answer.objects.get(id=a)
            Attempt.objects.create(quiz=quiz, attempter=attempter, question=question, answer=answer)
            attempt = Attempt.objects.get(quiz=quiz, attempter=attempter, question=question, answer=answer)
            attempts.append(attempt)
            total_score += question.points
            if answer.is_correct == True:

                attempter.score += question.points
                attempter.save()
            
        user_score = attempter.score
        quiz.attempts += 1
        quiz.total_average_score += (user_score/total_score) * 100
        quiz.average_score = quiz.total_average_score / quiz.attempts 
        quiz.save()

    context = {
        'quiz': quiz,
        'attempts': attempts,
        'user_score': user_score,
        'total_score': total_score,
    }

    return render(request, 'quiz/attemptdetail.html', context)



# pdf generator 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# create the views function for pdf generator
def QuizPdf(request, quiz_id):
    # Create a bytestream buffer
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    # Add some lines of text

    # get real cleaned_data
    quiz = get_object_or_404(Quizzes, id=quiz_id)


    lines = []

    lines.append('This quiz was created by ' + str(quiz.user))
    lines.append(str(quiz.title))
    lines.append(str(quiz.description))
    lines.append(" ")
    lines.append(f'Visit www.resersi.com/quiz/{quiz_id} to create and take quiz.')
    lines.append(" ")


    numberToAlpha = {
    '1':'a',
    '2':'b',
    '3':'c',
    '4':'d',
    '5':'e'
    }

    for question_index, question in enumerate(quiz.questions.all()):
        lines.append('(' + str(question_index + 1) + ') ' + str(question.question_text))

        for answer_index, answer in enumerate(question.answers.all()):
            lines.append('    (' + numberToAlpha[str(answer_index + 1)] + ')   ' + str(answer.answer_text))
        lines.append(" ")
            


    # loop 
    for line in lines:
        textob.textLine(line)

    # finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return Something
    return FileResponse(buf, as_attachment=True, filename=f"quiz/{quiz.title}.pdf")


