
# important method to deal with models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# the forms for each model
from .forms import NewQuizForm, NewQuestionForm, NewAnswerForm

# the models to be used to create the quiz app
from .models import Quizzes, Answer, Question, Attempter, Attempt

#Paginator

from django.core.paginator import Paginator

# django messages
from django.contrib import messages


# pdf generator

from django.http import HttpResponse

from django.views.generic import View

# import the utilities needed to create the quiz
from .utils import render_to_pdf
from django.template.loader import get_template

from diary.models import Diary


# make sure you add the question mode herein

# xhtml2pdf


class GeneratePDF(View):
    def get(self, request, quiz_id, *args, **kwargs):
        # template = get_template('quiz/takequiz.html')
        quiz = get_object_or_404(Quizzes, id=quiz_id)

        context = {
            'quiz': quiz,
        }
        # html = template.render(context)
        pdf = render_to_pdf('quiz/takequiz.html', context)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"quiz_{quiz.title}.pdf"
            # content = f"inline; filename={filename}"
            content = f"attachment; filename={filename}"
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found!")


















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










# the quiz list view
@login_required(login_url='login')
def QuizList(request):
    user = request.user
    quizzes = Quizzes.objects.all()# shuffle with .order_by('?')


    search_input= request.GET.get('search-area') or ''
    if search_input:
        quizzes = Quizzes.objects.filter(title__icontains=search_input)

    # create pagination
    p = Paginator(quizzes, 200)
    page = request.GET.get('page')
    quizzes = p.get_page(page)

    context={
        'search_input': search_input,
        'page_obj': quizzes,
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
        messages.info(request, 'Make sure you add an image!')
        

    context = {
        'form': form,
    }
    return render(request, 'quiz/newquiz.html', context)



# create an update quiz view
@login_required(login_url='login')
def UpdateQuiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    # quiz = Quizzes.objects.get(id=quiz_id)
    if request.user != quiz.user:
        return HttpResponseForbidden()
    
    form = NewQuizForm(instance=quiz)
    print(form)

    if request.method == 'POST':
        form = NewQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('quiz:quiz-detail', quiz_id=quiz.id)

    context = {
        'form': form,
        'quiz': quiz,
    }

    return render(request, 'quiz/updatequiz.html', context)



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
        messages.error(request, "You are not allowed to add questions to this quiz!")
        return HttpResponseForbidden()
    
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
            messages.error(request, "An error occurred!")
            messages.error(request, "Question not created!")


    else:
        form = NewQuestionForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'quiz/newquestion.html', context)





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


