from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import QTrueOrFalseQuestion, QFourChoicesQuestion

from django.contrib.auth.decorators import login_required

from django.db.models import Q

# the forms for each model
from .forms import NewQFourChoicesQuestionForm, NewQTrueOrFalseQuestionForm

# the models to be used to create the quiz app

from core.models import Streak, Profile
from analysis.models import UserPageCounter, PageCounter

# Utilities
from random import shuffle
from quiz.utils import sortKey


#Paginator

from django.core.paginator import Paginator

# django messages
from django.contrib import messages


# Create your views here.
"""
Generate image from the questions here.

"""



# the real test view
"""
Add all the documentation here

Whenever a question is created, an option to go live or add to draft should be presented to the user.
"""
@login_required(login_url='login')

def AnswerQuestion(request):
    user = request.user

    profile = Profile.objects.get(user=user)
           
    # add more logic to the questions here 
    # the Q and F function should be used here
    questions = []
    questions += QFourChoicesQuestion.objects.all()
    questions += QTrueOrFalseQuestion.objects.all()
    shuffle(questions)
    questions = questions[:1]

    """
    Create a logic to take care of accounts with less than 1 coins
    Add reward of 1,2,2,2,2,3,3,3,4,4,5
    """
    pagecounter = PageCounter.objects.get(id=1) # try PageCounter.objects.last()
    pagecounter.save()

    userpagecounter = UserPageCounter.objects.get(user=user)
    userpagecounter.save()

    context = {
        'questions': questions,
    }
    return render(request, 'question/takequestion.html', context)




"""
Add all the documentation here
"""
@login_required(login_url='login')

def QuestionCreate(request):
    return render(request, 'question/newquestion.html')





@login_required(login_url='login')

def FourChoicesQuestionCreate(request):
    user = request.user
    form = NewQFourChoicesQuestionForm()
    if request.method == 'POST':
        form = NewQFourChoicesQuestionForm(request.POST or None)
        if form.is_valid():
            question_text= form.cleaned_data.get('question_text')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            answer3=form.cleaned_data.get('answer3')
            answer4=form.cleaned_data.get('answer4')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration')
            solution=form.cleaned_data.get('solution')
            QFourChoicesQuestion.objects.create(user=user, question_text=question_text,
            answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4,
            correct=correct, points=points, duration=duration, solution=solution)


            return redirect('question:new-question')
    
    context= {
        'fourChoicesForm': form,
    }

    return render(request, 'question/fourChoicesQuestionCreate.html', context)






"""
Add all the documentation here
"""
@login_required(login_url='login')

def TrueOrFalseQuestionCreate(request):
    user = request.user
    form = NewQTrueOrFalseQuestionForm()
    if request.method == 'POST':
        form = NewQTrueOrFalseQuestionForm(request.POST)
        if form.is_valid(): 
            question_text= form.cleaned_data.get('question_text')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration')
            solution=form.cleaned_data.get('solution')

            QTrueOrFalseQuestion.objects.create(user=user, question_text=question_text,
            correct=correct, points=points, solution=solution, duration=duration)

            return redirect('question:new-question')
    
    context= {
        'trueOrFalseForm': form,
    }

    return render(request, 'question/trueOrFalseQuestionCreate.html', context)





"""
Add all the documentation here
"""
@login_required(login_url='login')

def FourChoicesQuestionUpdate(request, question_id):
    user = request.user
    question = get_object_or_404(QFourChoicesQuestion, id=question_id)
    
    fourChoicesForm = NewQFourChoicesQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewQFourChoicesQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()

            return redirect('profile')
    
    context= {
        'fourChoicesForm': fourChoicesForm,
    }

    return render(request, 'question/fourChoicesQuestionCreate.html', context)


@login_required(login_url='login')

def TrueOrFalseQuestionUpdate(request, question_id):
    user = request.user
    question = get_object_or_404(QTrueOrFalseQuestion, id=question_id)
    ftrueOrFalseForm = NewQTrueOrFalseQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewQFourChoicesQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()

            return redirect('profile')
    
    context= {
        'trueOrFalseForm': trueOrFalseForm,
    }

    return render(request, 'question/trueOrFalseQuestionCreate.html', context)




"""
Each question will be submitted here
value="{{question.form}}|{{question.id}}|answer1"
"""
from django.core import serializers
from django.forms.models import model_to_dict
def SubmitQuestion(request):
    print(request)
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        streak = Streak.objects.get(profile=profile)
        combination = tuple(answer.split('-'))
        print(combination)
        message = 'The answer is wrong!'
        print('It is working!')

        if combination[0] == 'fourChoicesQuestion':
            question = QFourChoicesQuestion.objects.get(id=combination[1])
            print(question)
            pos = combination[2]
            answer = question.getAnswer(pos)
            print(answer)
            print(combination[2])
            if question.correct == answer:
                streak.validateStreak()
                streak.save()
                messages.success(request, 'CORRECT!')
            else:
                messages.error(request, 'WRONG!')


        elif combination[0] == 'trueOrFalseQuestion':
            question = QTrueOrFalseQuestion.objects.get(id=combination[1])
            print(question)

            answer = question.getAnswer(combination[2])
            print(answer)
            print(combination[2])

            if question.correct == answer:
                print('The answer is correct!')
                streak.validateStreak()
                streak.save()
                messages.success(request, 'CORRECT!')
            else:
                messages.error(request, 'WRONG!')




                
        # import jsonresponse


    return redirect('question:answer-question')
    



        # model_to_dict{'': answer}