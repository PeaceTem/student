from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse

from .models import TrueOrFalseQuestion, FourChoicesQuestion

from django.contrib.auth.decorators import login_required

from django.db.models import Q, F, Count, Avg, Min, Max

# the forms for each model
from .forms import NewFourChoicesQuestionForm, NewTrueOrFalseQuestionForm, QuizGeneratorForm
from category.forms import NewCategoryForm
# the models to be used to create the quiz app

from core.models import Streak, Profile
from category.models import Category
from ads.models import PostAd

# celery tasks
from core.tasks import StreakValidator, CoinsTransaction, CreatorCoins

# Utilities
from random import shuffle
from quiz.utils import sortKey, randomCoin, adsRandom, randomChoice
from question.utils import randomQuestions
import decimal
#Paginator

from django.core.paginator import Paginator

# django messages
from django.contrib import messages



from django.core import serializers
from django.forms.models import model_to_dict

import json

# Create your views here.
"""
Generate image from the questions here.

"""



# the real test view
"""
Add all the documentation here

Whenever a question is created, an option to go live or add to draft should be presented to the user.
"""

@login_required(redirect_field_name='next' ,login_url='account_login')
def Question(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context={
        'nav': 'questions',
        'profile': profile,
    }

    return render(request, 'question/questions.html', context)




@login_required(redirect_field_name='next' ,login_url='account_login')
def MyQuestionList(request):
    user = request.user
    preQuestions = []
    preQuestions += FourChoicesQuestion.objects.filter(user=user, standalone=True)
    preQuestions += TrueOrFalseQuestion.objects.filter(user=user, standalone=True)
    questions = []
    for question in preQuestions:
        questions.append(tuple((question.date_created, question)))


    questions.sort(key=sortKey, reverse=True)
    # add reverse later
    print(questions)

    p = Paginator(questions, 2)
    page = request.GET.get('page')
    questions = p.get_page(page)

    context={
        'nav': 'my-questions',
        'page_obj': questions,
    }

    return render(request, 'question/myquestions.html', context)



def AnswerQuestion(request):
    # try:
    user = request.user
    decision = adsRandom()
    if decision == 'ads':
        return redirect('ads:postAd')
    questions = request.session.get('OldTownRoad')
    if len(questions) > 0:
        question = randomChoice(questions)
        questions.remove(question)
        request.session['OldTownRoad'] = questions

        context = {
        'question': question,
        }
        return render(request, 'question/takequestion.html', context)
    else:

        questions = []
        """
        Research how to prefetch and select related.
        And filters too 
        """
        questions += FourChoicesQuestion.objects.values("id", "form", "question", "answer1", "answer2", "answer3", "answer4", "solution", "duration_in_seconds", "attempts", "avgScore")[:10]

        questions += TrueOrFalseQuestion.objects.values("id", "form", "question", "answer1", "answer2", "solution", "duration_in_seconds", "attempts", "avgScore")[:10]

        shuffle(questions)
        question = randomChoice(questions)
        questions.remove(question)
        request.session['OldTownRoad'] = questions




    context = {
        'question': question,
    }
    return render(request, 'question/takequestion.html', context)




def CorrectionView(request, question_form, question_id, answer):
    if question_form == 'fourChoicesQuestion':
        question = FourChoicesQuestion.objects.get(id=question_id)
        print(question_form)
    elif question_form == 'trueOrFalseQuestion':
        question = TrueOrFalseQuestion.objects.get(id=question_id)
        print(question_form)


    answer = question.getAnswer(answer)
    
    postAd = PostAd.objects.all()
    postAd = randomChoice(postAd)
    print(postAd)

    

    context={
        'question': question,
        'postAd': postAd,
        'answer': answer,
    }

    return render(request, 'question/correction.html', context)


"""
Add all the documentation here
"""
@login_required(redirect_field_name='next' ,login_url='account_login')
def QuestionCreate(request):
    return render(request, 'question/newquestion.html')





@login_required(redirect_field_name='next' ,login_url='account_login')
def FourChoicesQuestionCreate(request):
    user = request.user
    form = NewFourChoicesQuestionForm()
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST or None)
        if form.is_valid():
            question= form.cleaned_data.get('question')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            answer3=form.cleaned_data.get('answer3')
            answer4=form.cleaned_data.get('answer4')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration_in_seconds')
            solution=form.cleaned_data.get('solution')
            shuffleAnswers = form.cleaned_data.get('shuffleAnswers')
            age_from = form.cleaned_data.get('age_from')
            age_to = form.cleaned_data.get('age_to')
            question = FourChoicesQuestion.objects.create(user=user, question=question,
            answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4,
            correct=correct, duration_in_seconds=duration, solution=solution, shuffleAnswers=shuffleAnswers,
            age_from=age_from, age_to=age_to, standalone=True)
            


            return redirect('question:category-create', question_id=f'fourChoices-{question.id}')
    
    context= {
        'fourChoicesForm': form,
    }
    print(form)
    return render(request, 'question/fourChoicesQuestionCreate.html', context)






"""
Add all the documentation here
"""
@login_required(redirect_field_name='next' ,login_url='account_login')
def TrueOrFalseQuestionCreate(request):
    user = request.user
    form = NewTrueOrFalseQuestionForm()
    if request.method == 'POST':
        form = NewTrueOrFalseQuestionForm(request.POST or None)
        if form.is_valid(): 
            question= form.cleaned_data.get('question')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration_in_seconds')
            solution=form.cleaned_data.get('solution')
            age_from = form.cleaned_data.get('age_from')
            age_to = form.cleaned_data.get('age_to')
            question = TrueOrFalseQuestion.objects.create(user=user, question=question,
            correct=correct, solution=solution, duration_in_seconds=duration, age_from=age_from, age_to=age_to, standalone=True)

            return redirect('question:category-create', question_id=f'trueOrFalse-{question.id}')

    
    context= {
        'trueOrFalseForm': form,
    }

    return render(request, 'question/trueOrFalseQuestionCreate.html', context)





"""
Add all the documentation here
"""
@login_required(redirect_field_name='next' ,login_url='account_login')
def CategoryCreate(request, question_id):
    print('The question is relayed to the category view')
    user = request.user
    profile = Profile.objects.get(user=user)
    question_id = question_id.split('-')
    if question_id[0] == 'trueOrFalse':
        question = TrueOrFalseQuestion.objects.get(id=question_id[1])
    elif question_id[0] == 'fourChoices':
        question = FourChoicesQuestion.objects.get(id=question_id[1])

    form = NewCategoryForm()
    categories = Category.objects.all()

    title = request.GET.get('newCategory') or ''
    title = title.strip()
    title = title.split(' ')
    title = '-'.join(title)
    if title:
        if question.categories.all().count() < 5:
            category = None

            try:
                print('trying to get the title')
                newCategory = Category.objects.get(title__iexact=title)
                print('gotten the title')
                print(newCategory)
                if not newCategory in question.categories.all():

                    question.categories.add(newCategory)
                    question.save()
                    newCategory.number_of_questions += 1
                    newCategory.save()
                    if profile.categories.all().count() > 99:
                        removed = profile.categories.first()
                        profile.categories.remove(removed)
                    profile.categories.add(newCategory)
                    profile.save()
                else:
                    messages.warning(request, f"{newCategory.title} has already been added to the question!")
                # return a message that it is already created
            except:
                newCategory = Category.objects.create(registered_by=user, title=title)
                question.categories.add(newCategory)
                question.save()
                newCategory.number_of_questions += 1
                newCategory.save()
                if profile.categories.all().count() > 99:
                    removed = profile.categories.first()
                    profile.categories.remove(removed)
                profile.categories.add(newCategory)
                profile.save()


    # create pagination
    questionCategories = question.categories.all()
    addedCategories = request.GET.getlist('addedCategories') or ''
    if addedCategories:
        
        for category in questionCategories:
            if category not in addedCategories:
                question.categories.remove(category)
                category.number_of_questions -= 1
                category.save()

        for cart in addedCategories:
            category = None
            if question.categories.all().count() < 5:
                try:
                    category = Category.objects.get(title__iexact=cart)
                except:
                    pass
                if category:
                    if category not in question.categories.all():
                        question.categories.add(category)
                        question.save()
                        category.number_of_questions += 1
                        category.save()
                        if profile.categories.all().count() > 99:
                            removed = profile.categories.first()
                            profile.categories.remove(removed)
                        profile.categories.add(category)
                        profile.save()

        
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
@login_required(redirect_field_name='next' ,login_url='account_login')
def FourChoicesQuestionUpdate(request, question_id):
    user = request.user
    question = get_object_or_404(FourChoicesQuestion, id=question_id)
    
    fourChoicesForm = NewFourChoicesQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST or None, instance=question)
        if form.is_valid():
            form.save()

            return redirect('question:category-create', question_id=f'fourChoices-{question.id}')

    
    context= {
        'fourChoicesForm': fourChoicesForm,
    }

    return render(request, 'question/fourChoicesQuestionCreate.html', context)


@login_required(redirect_field_name='next' ,login_url='account_login')
def TrueOrFalseQuestionUpdate(request, question_id):
    user = request.user
    question = get_object_or_404(QTrueOrFalseQuestion, id=question_id)
    trueOrFalseForm = NewTrueOrFalseQuestionForm(instance=question)
    print('trueOrFalseForm')
    if request.method == 'POST':
        form = NewTrueOrFalseQuestionForm(request.POST or None, instance=question)
        print('form')
        if form.is_valid():
            print('another form')
            form.save()
            print('form save')
        

            return redirect('question:category-create', question_id=f'trueOrFalse-{question.id}')

    
    context= {
        'trueOrFalseForm': trueOrFalseForm,
    }

    return render(request, 'question/trueOrFalseQuestionCreate.html', context)




@login_required(redirect_field_name='next' ,login_url='account_login')
def DeleteQuestion(request,question_form, question_id):
    user =request.user
    if question_form == 'fourChoices':
        question = FourChoicesQuestion.objects.get(id=question_id)
    elif question_form == 'trueOrFalse':
        question = TrueOrFalseQuestion.objects.get(id=question_id)
    if request.method == 'POST':
        question.delete()
        # messages.success(request, "You've successfully deleted a question!")
        return HttpResponse('Deleted!')

    context={
        'obj': question,
    }

    return render(request, 'question/delete.html', context)


"""

Each question will be submitted here
value="{{question.form}}|{{question.id}}|answer1"
"""
def SubmitQuestion(request):



    try:
        user = request.user
        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
        if request.method == 'POST':
            answer = request.POST.get('answer')

            if user.is_authenticated:
                # streak = Streak.objects.get(profile=profile)
                profile.questionAttempts += 1
            combination = tuple(answer.split('-'))
            message = 'The answer is wrong!'

            if combination[0] == 'fourChoicesQuestion':
                question = FourChoicesQuestion.objects.get(id=combination[1])
                pos = combination[2]
                question.attempts += 1
                    
                if pos == 'answer1':
                    question.answer1NumberOfTimesTaken += 1
                elif pos == 'answer2':
                    question.answer2NumberOfTimesTaken += 1
                elif pos == 'answer3':
                    question.answer3NumberOfTimesTaken += 1
                elif pos == 'answer4':
                    question.answer4NumberOfTimesTaken += 1


                question.save()


                for category in question.categories.all():
                    category.question_number_of_times_taken += 1
                    category.save()
                    
                if question.correct == pos:

                    





                    question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:
                        creator = Profile.objects.select_related('user').get(user=question.user)
                        if profile.fourChoicesQuestionsTaken.all().count() > 999:
                            remove = profile.fourChoicesQuestionsTaken.first()
                            profile.fourChoicesQuestionsTaken.remove(removed)
                        profile.fourChoicesQuestionsTaken.add(question)
                            
                        if profile.user != question.user:
                            # streak.validateStreak()
                            # streak.save()
                            """
                            This is a celery task
                            """
                            StreakValidator.delay(profile)




                            value = randomCoin()
                            profile.coins += value
                            profile.questionAvgScore = decimal.Decimal(round(((profile.questionAvgScore * (profile.questionAttempts - 1)) + 100) / profile.questionAttempts ,1))
                            
                            profile.save()
                            """
                            This is a celery tasks
                            don't remove the previous task ooo because it is different from this celery task
                            """
                            CoinsTransaction.delay(user, value)






                            if question.avgScore >= 50:
                                creator.coins += decimal.Decimal(0.10)
                                creator.save()
                                CreatorCoins.delay(creator.user, value)
                                print(creator.coins)
                            messages.success(request, f"You've received {value} coins")

                    messages.success(request, 'CORRECT!')
                    
                else:
                    question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:
                        
                        profile.coins -= 1
                        profile.questionAvgScore = decimal.Decimal(round((profile.questionAvgScore * (profile.questionAttempts - 1)) / profile.questionAttempts ,1))
                        if profile.fourChoicesQuestionsMissed.all().count() > 999:
                            remove = profile.fourChoicesQuestionsMissed.first()
                            profile.fourChoicesQuestionsMissed.remove(removed)
                        profile.fourChoicesQuestionsMissed.add(question)
                        profile.save()

                        messages.warning(request, f"You've lost 1 coin")
                    messages.error(request, 'WRONG!')
                    return redirect('question:correction', question_form=combination[0], question_id=combination[1], answer=combination[2])


            elif combination[0] == 'trueOrFalseQuestion':
                question = TrueOrFalseQuestion.objects.get(id=combination[1])
                pos = combination[2]
                question.attempts += 1
                    
                if pos == 'answer1':
                    question.answer1NumberOfTimesTaken += 1
                elif pos == 'answer2':
                    question.answer2NumberOfTimesTaken += 1


                question.save()

                for category in question.categories.all():
                    category.question_number_of_times_taken += 1
                    category.save()

                
                answer = question.getAnswer(pos)

                if question.correct == answer:

                    

                    question.avgScore = round(((question.avgScore *(question.attempts - 1) + 100) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:
                        
                        if profile.trueOrFalseQuestionsTaken.all().count() > 999:
                            remove = profile.trueOrFalseQuestionsTaken.first()
                            profile.trueOrFalseQuestionsTaken.remove(removed)
                        profile.trueOrFalseQuestionsTaken.add(question)
                            
                        if profile.user != question.user:
                            streak.validateStreak()
                            streak.save()
                            """
                            This is a celery task
                            """

                            StreakValidator.delay(profile)



                            value = randomCoin()
                            profile.coins += value
                            profile.questionAvgScore = decimal.Decimal(round(((profile.questionAvgScore * (profile.questionAttempts - 1)) + 100) / profile.questionAttempts ,1))
                            
                            profile.save()
                            """
                            This is a celery tasks
                            don't remove the previous task ooo because it is different from this celery task
                            """
                            CoinsTransaction.delay(user, value)



                            if question.avgScore >= 50:
                                creator = Profile.objects.select_related('user').get(user=question.user)

                                creator.coins += decimal.Decimal(0.10)
                                creator.save()
                                CreatorCoins.delay(creator.user, value)
                            messages.success(request, f"You've received {value} coins")

                    messages.success(request, 'CORRECT!')
                    
                else:
                    question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                    question.save()

                    if user.is_authenticated:
                        profile.coins -= 1
                        if profile.trueOrFalseQuestionsMissed.all().count() > 999:
                            remove = profile.trueOrFalseQuestionsMissed.first()
                            profile.trueOrFalseQuestionsMissed.remove(removed)
                        profile.trueOrFalseQuestionsMissed.add(question)
                        profile.questionAvgScore = decimal.Decimal(round((profile.questionAvgScore * (profile.questionAttempts - 1)) / profile.questionAttempts ,1))
                        profile.save()
                        messages.warning(request, f"You've lost 1 coin")
                    messages.error(request, 'WRONG!')
                    return redirect('question:correction', question_form=combination[0], question_id=combination[1], answer=combination[2])

    except:
        pass

    return redirect('question:answer-question')





#  & Q(solution_quality__gt=0)
def QuizGenerator(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.prefetch_related('categories', 'trueOrFalseQuestionsTaken', 'trueOrFalseQuestionsMissed', 'fourChoicesQuestionsTaken', 'fourChoicesQuestionsMissed').get(user=user)

        categories = profile.categories.all().order_by('title')
    else:
        categories = Category.objects.all().order_by('quiz_number_of_times_taken')[:25]
    form = QuizGeneratorForm()

    if request.method == 'POST':
        try:
            form = QuizGeneratorForm(request.POST)

            if form.is_valid():
                duration_in_minutes = form.cleaned_data.get('duration_in_minutes')
                number_of_questions = form.cleaned_data.get('number_of_questions')
                categories = request.POST.getlist('categories')
                print(duration_in_minutes, number_of_questions)
                trueOrFalseQuestions = TrueOrFalseQuestion.objects.none()
                fourChoicesQuestions = FourChoicesQuestion.objects.none()
                for category in categories:
                    lookup = Q(categories__title=category, solution_quality__gt=0)
                    trueOrFalseQuestions |= TrueOrFalseQuestion.objects.filter(lookup).distinct()[:1000]
                    fourChoicesQuestions |= FourChoicesQuestion.objects.filter(lookup).distinct()[:1000]
                trueOrFalseQuestions = trueOrFalseQuestions.distinct()
                fourChoicesQuestions = fourChoicesQuestions.distinct()


                trueOrFalseQuestionsTaken = profile.trueOrFalseQuestionsTaken.all()
                trueOrFalseQuestionsMissed = profile.trueOrFalseQuestionsMissed.all()
                fourChoicesQuestionsTaken = profile.fourChoicesQuestionsTaken.all()
                fourChoicesQuestionsMissed = profile.fourChoicesQuestionsMissed.all()
                questionsList = [*trueOrFalseQuestionsTaken, *trueOrFalseQuestionsMissed, *fourChoicesQuestionsTaken, *fourChoicesQuestionsMissed]

                questionSet = list((*trueOrFalseQuestions, *fourChoicesQuestions))



            

                questions = []
                i = 0
                while len(questions) < number_of_questions and len(questionSet) > 0:
                    question = randomChoice(questionSet)
                    questionSet.remove(question)
                    if (question not in questions) and (question not in questionsList):
                        questions.append(tuple((i, question)))
                        i += 1

                
                # questions = randomQuestions(questionSet, number_of_questions)
                questionLength = len(questions)
                if questionLength < number_of_questions:
                    messages.info(request, 'The questions are insufficient!')

                request.session['duration'] = duration_in_minutes
                request.session['questionLength'] = questionLength
                sessionQuestions = []
                for question in questions:
                    
                    q = tuple((question[0], tuple((question[1].form, question[1].id))))
                    sessionQuestions.append(q)
                request.session['questions'] = sessionQuestions
                
                print(request.session['questions'], request.session['duration'])

                # print(shuffle([1,2,3,4]))

                context = {
                'questions': questions,
                'duration': duration_in_minutes,
                'questionLength': questionLength,
                'reAttempt': 'no',
                'type': 'reAttempt',
                }
            return render(request, 'question/quiz.html', context)

        except:
            messages.error(request, 'There are no questions available!')
            return redirect('question:questions')
            

    context={
        'form': form,
        'categories': categories,
    }

    return render(request, 'question/quizGenerator.html', context)




def ReAttemptQuiz(request):
    if request.method == 'POST':

        questions = request.session['questions']
        duration = request.session['duration']
        questionLength = request.session['questionLength']
        print(questions, duration)
        sessionQuestions = []
        for question in questions:
            index = question[0]
            if question[1][0] == 'trueOrFalseQuestion':
                q = TrueOrFalseQuestion.objects.get(id=question[1][1])
            elif question[1][0] == 'fourChoicesQuestion':
                q = FourChoicesQuestion.objects.get(id=question[1][1])
            pack_question = tuple((index, q))
            sessionQuestions.append(pack_question)



        context = {
                'questions': sessionQuestions,
                'duration': duration,
                'questionLength': questionLength,
                'reAttempt': 'yes',
                'type': 'reAttempt',
        }
        return render(request, 'question/quiz.html', context)




@login_required(redirect_field_name='next' , login_url='account_login')
def PastQuestions(request):
    try:
        user = request.user
        profile = Profile.objects.prefetch_related('trueOrFalseQuestionsTaken', 'trueOrFalseQuestionsMissed', 'fourChoicesQuestionsTaken', 'fourChoicesQuestionsMissed').get(user=user)

        trueOrFalseQuestionsTaken = profile.trueOrFalseQuestionsTaken.all()
        trueOrFalseQuestionsMissed = profile.trueOrFalseQuestionsMissed.all()
        fourChoicesQuestionsTaken = profile.fourChoicesQuestionsTaken.all()
        fourChoicesQuestionsMissed = profile.fourChoicesQuestionsMissed.all()

        questionsList = [*trueOrFalseQuestionsTaken, *trueOrFalseQuestionsMissed, *fourChoicesQuestionsTaken, *fourChoicesQuestionsMissed]

        questions = []

        i = 0

        while (len(questions) < 10) and (len(questionsList) > 0):

            question = randomChoice(questionsList)
            questionsList.remove(question)
            print(question)
            if question not in questions:
                questions.append(tuple((i, question)))
                i += 1

        questionLength = len(questions)
        if questionLength < 10:
            messages.info(request, 'The questions are insufficient!')


        duration = 0
        for question in questions:
            duration += question[1].duration_in_seconds
    except:
        messages.error(request, 'There are no questions available!')
        return redirect('question:questions')
        
    context = {
        'questions': questions,
        'duration': duration,
        'questionLength': questionLength,
        'type': 'pastQuestions',

    }
    return render(request, 'question/quiz.html', context)

    






def SubmitQuizGenerator(request, ref_code, *args, **kwargs):
    user = request.user
    if request.method == 'GET':
        if not user.is_authenticated:
            code = str(kwargs.get('ref_code'))
            ReferralService(code)   
        return redirect('question:quiz-generator')

    
    if request.method == 'POST':
        if user.is_authenticated:
            profile = get_object_or_404(Profile, user=user)
            # streak = Streak.objects.get(profile=profile)
    
    
        score = 0
        postAd = PostAd.objects.all()
        postAd = randomChoice(postAd)

        answers = request.POST.getlist('answer')
        reAttempt = request.POST.get('reAttempt')
        questionLength = request.POST.get('questionLength')
        questionType = request.POST.get('type')

        print(reAttempt, 'This is reAttempt')
        questionsList = []
  
        for answer in answers:
            combination = tuple(answer.split('-'))
            
            if combination[0] == 'fourChoices':
                question = FourChoicesQuestion.objects.get(id=combination[1])
                pos = combination[2]

                question.attempts += 1

                if pos == 'answer1':
                    question.answer1NumberOfTimesTaken += 1
                elif pos == 'answer2':
                    question.answer2NumberOfTimesTaken += 1
                elif pos == 'answer3':
                    question.answer3NumberOfTimesTaken += 1
                elif pos == 'answer4':
                    question.answer4NumberOfTimesTaken += 1



                question.save()

                for category in question.categories.all():
                    category.question_number_of_times_taken += 1
                    category.save()
                    
                answer = question.getAnswer(pos)
                questionsList.append((question, answer))
                if question.correct == combination[2]:
                    score += 1


                    question.avgScore = round(((question.avgScore *(question.attempts - 1) + 100) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:

                        if (question.user != profile.user) and (questionType != 'pastQuestions'):
                            profile.questionAttempts += 1
                                                  
                            creator = Profile.objects.get(user=question.user)
                            profile.questionAvgScore = decimal.Decimal(round(((profile.questionAvgScore * (profile.questionAttempts - 1)) + 100) / profile.questionAttempts ,1))
                            profile.save()
                            if question.avgScore >= 50:
                                creator.coins += decimal.Decimal(0.10)
                                creator.save()
                                CreatorCoins.delay(creator.user, value)


                            if profile.fourChoicesQuestionsTaken.all().count() > 999:
                                remove = profile.fourChoicesQuestionsTaken.first()
                                profile.fourChoicesQuestionsTaken.remove(removed)
                            profile.fourChoicesQuestionsTaken.add(question)
                            # streak.validateStreak()
                            # streak.save()
                            """
                            This is a celery task
                            """
                            StreakValidator.delay(profile)





                else:
                    question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:
                        

                        if question.user != profile.user:
                            profile.questionAttempts += 1
                            profile.questionAvgScore = decimal.Decimal(round((profile.questionAvgScore * (profile.questionAttempts - 1)) / profile.questionAttempts ,1))


                        if profile.fourChoicesQuestionsMissed.all().count() > 999:
                                removed = profile.fourChoicesQuestionsMissed.first()
                                profile.fourChoicesQuestionsMissed.remove(removed)
                        profile.fourChoicesQuestionsMissed.add(question)
                        

                    
            elif combination[0] == 'trueOrFalse':
                question = TrueOrFalseQuestion.objects.get(id=combination[1])
                pos = combination[2]

                question.attempts += 1

                if pos == 'answer1':
                    question.answer1NumberOfTimesTaken += 1
                elif pos == 'answer2':
                    question.answer2NumberOfTimesTaken += 1


                question.save()

                for category in question.categories.all():
                    category.question_number_of_times_taken += 1
                    category.save()
                    
                answer = question.getAnswer(combination[2])
                questionsList.append((question, answer))
                if question.correct == answer:
                    score += 1
                    question.avgScore = round(((question.avgScore *(question.attempts - 1) + 100) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:
                    
                        if (question.user != profile.user) and (questionType != 'pastQuestions'):
                            profile.questionAttempts += 1
                                                  
                            creator = Profile.objects.get(user=question.user)
                            profile.questionAvgScore = decimal.Decimal(round(((profile.questionAvgScore * (profile.questionAttempts - 1)) + 100) / profile.questionAttempts ,1))
                            profile.save()
                            if question.avgScore >= 50:
                                creator.coins += decimal.Decimal(0.10)
                                creator.save()
                                CreatorCoins.delay(creator.user, value)


                            if profile.trueOrFalseQuestionsTaken.all().count() > 999:
                                remove = profile.trueOrFalseQuestionsTaken.first()
                                profile.trueOrFalseQuestionsTaken.remove(removed)
                            profile.trueOrFalseQuestionsTaken.add(question)
                            # streak.validateStreak()
                            # streak.save()
                            """
                            This is a celery task
                            """
                            StreakValidator.delay(profile)





                else:
                    question.avgScore = round((question.avgScore *(question.attempts - 1) / question.attempts), 1)
                    question.save()
                    if user.is_authenticated:
                        if question.user != profile.user:
                            profile.questionAttempts += 1
                            profile.questionAvgScore = decimal.Decimal(round((profile.questionAvgScore * (profile.questionAttempts - 1)) / profile.questionAttempts ,1))


                        if profile.trueOrFalseQuestionsMissed.all().count() > 999:
                                remove = profile.trueOrFalseQuestionsMissed.first()
                                profile.trueOrFalseQuestionsMissed.remove(removed)
                        profile.trueOrFalseQuestionsMissed.add(question)
                   


        total_score = int(questionLength)
        user_score = score
        if user.is_authenticated:
            try:
                user_avg_score = (user_score/total_score) * 100
                if user_avg_score > 50 and reAttempt == 'no':
                        value = user_score
                        profile.coins += decimal.Decimal(value)
                        profile.save()
                        messages.success(request, f"You've won {value} coins!")
                        """
                        This is a celery tasks
                        don't remove the previous task ooo because it is different from this celery task
                        """
                        CoinsTransaction.delay(user, value)

            except ZeroDivisionError:
                
                messages.error(request, "You didn't answer any question.")
                return redirect('quiz:take-quiz', quiz_id = quiz.id)
        

        attempt_report = f"You answered {len(answers)} out of {questionLength} questions"
                   
        context = {
            'user_score': user_score,
            'user_avg_score': user_avg_score,
            'total_score': total_score,
            'questionsList': questionsList,
            'postAd': postAd,
            'attempt_report': attempt_report,
            'questionLength': questionLength,
            'type': questionType,
        }

        
    return render(request, 'question/submitQuiz.html', context)







@login_required(redirect_field_name='next' ,login_url='account_login')
def SolutionQuality(request, question_form, question_id):
    user = request.user
    if user.is_authenticated:

        if question_form == 'fourChoices':
            question = FourChoicesQuestion.objects.prefetch_related('solution_validators').get(id=question_id)
        elif question_form == 'trueOrFalse':
            question = TrueOrFalseQuestion.objects.prefetch_related('solution_validators').get(id=question_id)

        quality = request.GET.get('quality')
        print(quality)

        if quality == 'Yes':
            question.solution_quality += 1
            question.solution_validators.add(user)

        elif quality == 'No':
            question.solution_quality -= 1
            question.solution_validators.add(user)
        
        question.save()

    return HttpResponse('Modified Solution Quality!')



def TestQuestion(request):
    question1 = FourChoicesQuestion.objects.values("id", "user", "form", "question", "answer1", "answer2", "answer3", "answer4", "solution", "duration_in_seconds", "attempts", "avgScore")

    question2 = TrueOrFalseQuestion.objects.values("id", "user", "form", "question", "answer1", "answer2", "solution", "duration_in_seconds", "attempts", "avgScore")

    questions = [*question1, *question2]
    print(questions)
    context = {
        'questions': questions,
    }
    return render(request, 'question/testquestion.html', context)







def TCorrectionView(request, question_form, question_id, answer):
    if question_form == 'fourChoicesQuestion':
        question = FourChoicesQuestion.objects.get(id=question_id)
        print(question_form)
    elif question_form == 'trueOrFalseQuestion':
        question = TrueOrFalseQuestion.objects.get(id=question_id)
        print(question_form)


    answer = question.getAnswer(answer)
    
    postAd = PostAd.objects.all()
    postAd = randomChoice(postAd)
    print(postAd)

    

    context={
        'question': question,
        'postAd': postAd,
        'answer': answer,
    }

    return render(request, 'question/correction.html', context)

