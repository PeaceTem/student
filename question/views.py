from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import QTrueOrFalseQuestion, QFourChoicesQuestion

from django.contrib.auth.decorators import login_required

from django.db.models import Q

# the forms for each model
from .forms import NewQFourChoicesQuestionForm, NewQTrueOrFalseQuestionForm
from quiz.forms import NewCategoryForm
# the models to be used to create the quiz app

from core.models import Streak, Profile
from quiz.models import Category 
# Utilities
from random import shuffle
from quiz.utils import sortKey, randomCoin, adsRandom, randomChoice

import decimal
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
def AnswerQuestion(request):
    user = request.user
    decision = adsRandom()
    if decision == 'ads':
        return redirect('ads:postAd')

    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        if profile.coins <= 0:
            messages.error(request, 'You have no coins left to take more questions.')
            redirect('quiz:quizzes')
           
    # add more logic to the questions here 
    # the Q and F function should be used here
    questions = []
    questions += QFourChoicesQuestion.objects.all()
    questions += QTrueOrFalseQuestion.objects.all()
    # random 

    question = randomChoice(questions)
    """
    Create a logic to take care of accounts with less than 1 coins
    Add reward of 1,2,2,2,2,3,3,3,4,4,5
    """
 
    context = {
        'question': question,
    }
    return render(request, 'question/takequestion.html', context)




"""
Add all the documentation here
"""
@login_required(redirect_field_name='next' ,login_url='account_login')
def QuestionCreate(request):
    return render(request, 'question/newquestion.html')





@login_required(login_url='account_login')
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
            question = QFourChoicesQuestion.objects.create(user=user, question_text=question_text,
            answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4,
            correct=correct, duration=duration, solution=solution)


            return redirect('question:category-create', question_id=f'fourChoices-{question.id}')
    
    context= {
        'fourChoicesForm': form,
    }

    return render(request, 'question/fourChoicesQuestionCreate.html', context)






"""
Add all the documentation here
"""
@login_required(login_url='account_login')
def TrueOrFalseQuestionCreate(request):
    user = request.user
    form = NewQTrueOrFalseQuestionForm()
    if request.method == 'POST':
        form = NewQTrueOrFalseQuestionForm(request.POST or None)
        if form.is_valid(): 
            question_text= form.cleaned_data.get('question_text')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration')
            solution=form.cleaned_data.get('solution')

            question = QTrueOrFalseQuestion.objects.create(user=user, question_text=question_text,
            correct=correct, solution=solution, duration=duration)

            return redirect('question:category-create', question_id=f'trueOrFalse-{question.id}')

    
    context= {
        'trueOrFalseForm': form,
    }

    return render(request, 'question/trueOrFalseQuestionCreate.html', context)





"""
Add all the documentation here
"""
@login_required(login_url='account_login')
def CategoryCreate(request, question_id):
    user = request.user
    question_id = question_id.split('-')
    if question_id[0] == 'trueOrFalse':
        question = QTrueOrFalseQuestion.objects.get(id=question_id[1])
    elif question_id[0] == 'fourChoices':
        question = QFourChoicesQuestion.objects.get(id=question_id[1])

    form = NewCategoryForm()
    categories = Category.objects.all()

    title = request.GET.get('newCategory') or ''
    title = title.strip()
    title = title.split(' ')
    title = '-'.join(title)
    if title:

        try:
            Category.objects.get(title__icontains=title)
            # return a message that it is already created
        except:
            newCategory = Category.objects.create(registered_by=user, title=title)
            question.categories.add(newCategory)
            question.save()


    # create pagination
    questionCategories = question.categories.all()
    addedCategories = request.GET.getlist('addedCategories') or ''
    if addedCategories:
        
        for category in questionCategories:
            if category not in addedCategories:
                question.categories.remove(category)

        for cart in addedCategories:
            if question.categories.all().count() < 3:
                category = Category.objects.get(title__exact=cart) or None
                if category:
                    if category not in question.categories.all():
                        question.categories.add(category)
                        question.save()

        
    questionCategories = question.categories.all()


    context= {
        'page_obj': categories,
        'questionCategories' : questionCategories,
        'question': question,

    }
    # question:new-question

    return render(request, 'question/categoryCreate.html', context)







"""
Add all the documentation here
"""
@login_required(login_url='account_login')
def FourChoicesQuestionUpdate(request, question_id):
    user = request.user
    question = get_object_or_404(QFourChoicesQuestion, id=question_id)
    
    fourChoicesForm = NewQFourChoicesQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewQFourChoicesQuestionForm(request.POST or None, instance=question)
        if form.is_valid():
            form.save()

            return redirect('question:category-create', question_id=f'fourChoices-{question.id}')

    
    context= {
        'fourChoicesForm': fourChoicesForm,
    }

    return render(request, 'question/fourChoicesQuestionCreate.html', context)


@login_required(login_url='account_login')
def TrueOrFalseQuestionUpdate(request, question_id):
    user = request.user
    question = get_object_or_404(QTrueOrFalseQuestion, id=question_id)
    trueOrFalseForm = NewQTrueOrFalseQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewQFourChoicesQuestionForm(request.POST or None, instance=question)
        if form.is_valid():
            form.save()

            return redirect('question:category-create', question_id=f'trueOrFalse-{question.id}')

    
    context= {
        'trueOrFalseForm': trueOrFalseForm,
    }

    return render(request, 'question/trueOrFalseQuestionCreate.html', context)




@login_required(login_url='account_login')
def DeleteQuestion(request,question_form, question_id):
    user =request.user
    if question_form == 'fourChoices':
        question = QFourChoicesQuestion.objects.get(id=question_id)
    elif question_form == 'trueOrFalse':
        question = QTrueOrFalseQuestion.objects.get(id=question_id)
    if request.method == 'POST':
        question.delete()
        messages.success(request, "You've successfully delete a question!")
        return redirect('profile')

    context={
        'obj': question,
    }

    return render(request, 'question/delete.html', context)


"""
Each question will be submitted here
value="{{question.form}}|{{question.id}}|answer1"
"""
from django.core import serializers
from django.forms.models import model_to_dict
def SubmitQuestion(request):
    try:
        user = request.user
        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
        if request.method == 'POST':
            answer = request.POST.get('answer')
            if user.is_authenticated:
                streak = Streak.objects.get(profile=profile)
                profile.questionAttempts += 1
            combination = tuple(answer.split('-'))
            message = 'The answer is wrong!'

            if combination[0] == 'fourChoicesQuestion':
                question = QFourChoicesQuestion.objects.get(id=combination[1])
                question.attempts += 1
                question.save()
                if question.correct == combination[2]:
                    if user.is_authenticated:
                        question.avgScore = round(((question.avgScore *(question.attempts - 1) + 100) / question.attempts), 1)
                        question.save()
                        creator = Profile.objects.get(user=question.user)
                        if profile.user != question.user:
                            streak.validateStreak()
                            streak.save()
                            value = randomCoin()
                            profile.coins += value
                            profile.questionAvgScore = decimal.Decimal(round(((profile.questionAvgScore * (profile.questionAttempts - 1)) + 100) / profile.questionAttempts ,1))
                            profile.save()
                            if question.avgScore >= 60:
                                creator.coins += decimal.Decimal(0.10)
                                creator.save()
                                print(creator.coins)
                            messages.success(request, f"You've received {value} coins")

                    messages.success(request, 'CORRECT!')
                    
                else:
                    if user.is_authenticated:
                        question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                        question.save()
                        profile.coins -= 1
                        profile.questionAvgScore = decimal.Decimal(round((profile.questionAvgScore * (profile.questionAttempts - 1)) / profile.questionAttempts ,1))
                        profile.fourChoicesQuestionsMissed.add(question)
                        profile.save()
                        messages.warning(request, f"You've lost 1 coin")
                    messages.error(request, 'WRONG!')


            elif combination[0] == 'trueOrFalseQuestion':
                question = QTrueOrFalseQuestion.objects.get(id=combination[1])
                question.attempts += 1
                question.save()
                answer = question.getAnswer(combination[2])

                if question.correct == answer:
                    if user.is_authenticated:
                        question.avgScore = round(((question.avgScore *(question.attempts - 1) + 100) / question.attempts), 1)
                        question.save()
                        creator = Profile.objects.get(user=question.user)
                        if profile.user != question.user:
                            streak.validateStreak()
                            streak.save()
                            value = randomCoin()
                            profile.coins += value
                            profile.questionAvgScore = decimal.Decimal(round(((profile.questionAvgScore * (profile.questionAttempts - 1)) + 100) / profile.questionAttempts ,1))
                            profile.save()
                            if question.avgScore >= 60:
                                creator.coins += decimal.Decimal(0.10)
                                creator.save()
                            messages.success(request, f"You've received {value} coins")

                    messages.success(request, 'CORRECT!')
                    
                else:
                    if user.is_authenticated:
                        question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                        question.save()
                        profile.coins -= 1
                        profile.trueOrFalseQuestionsMissed.add(question)
                        profile.questionAvgScore = decimal.Decimal(round((profile.questionAvgScore * (profile.questionAttempts - 1)) / profile.questionAttempts ,1))
                        profile.save()
                        messages.warning(request, f"You've lost 1 coin")
                    messages.error(request, 'WRONG!')
    except:
        pass

    return redirect('question:answer-question')