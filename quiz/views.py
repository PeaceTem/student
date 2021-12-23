
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# function based views
from .forms import NewQuizForm, NewQuestionForm, NewAnswerForm

from django.views.generic.list import ListView

from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from .models import Quizzes, Answer, Question, Attempter, Attempt

"""# pdf generator 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# create the views function for pdf generator
def quiz_pdf(request):
    # Create a bytestream buffer
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # creatin a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    # Add some lines of text
    lines = [
        "This is line 1",
        "This is line 2",
        "This is line 3",
        "This is line 4",
        "This is line 5"
    ]

    # get real cleaned_data
    quizzes = Quiz.objects.all()

    lines = []

    for quiz in quizzes:
        lines.append(quiz.user)
        lines.append(quiz.title)
        lines.append(quiz.description)
        lines.append(quiz.date)
        lines.append(quiz.due)
        lines.append(quiz.allowed_attempts)
        lines.append(quiz.time_limit_mins)
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
    return FileResponse(buf, as_attachment=True, filename="quiz.pdf")"""



class QuizList(ListView):
    model = Quizzes
    context_object_name = 'quizzes'


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'quiz/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('quizzes')


class RegisterPage(FormView):
    template_name = 'quiz/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('quizzes')

    def form_valid(self, form):
        user = form.save()
        # logs the user in after registration
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('quizzes')
        return super(RegisterPage, self).get(*args, **kwargs)



def NewQuiz(request):
    user = request.user
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            description=form.cleaned_data.get('description')
            quiz = Quizzes.objects.create(user=user, title=title, description=description)
            return redirect('new-question', quiz_id=quiz.id)

    else:
        form = NewQuizForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/newquiz.html', context)

def NewQuestion(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
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
            return redirect('new-question', quiz_id=quiz.id)

    else:
        form = NewQuestionForm()
    context = {
        'form': form,
    }
    
    return render(request, 'quiz/newquestion.html', context)



def QuizDetail(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    my_attempts = Attempter.objects.filter(quiz=quiz, user=user)

    context = {
        'quiz': quiz,
        'my_attempts': my_attempts,
    }
    return render(request, 'quiz/quizdetail.html', context)

def TakeQuiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    context = {
        'quiz': quiz,
    }
    return render(request, 'quiz/takequiz.html', context)


def SubmitAttempt(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    earned_points = 0
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
            if answer.is_correct == True:

                attempter.score += question.points
                attempter.save()
            
        total_score = attempter.score

    context = {
        'quiz': quiz,
        'attempts': attempts,
        'total_score': total_score,
    }

    return render(request, 'quiz/attemptdetail.html', context)

