
# important method to deal with models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q

# the forms for each model
from .forms import NewQuizForm, NewCategoryForm, NewFourChoicesQuestionForm, NewTrueOrFalseQuestionForm


# the models to be used to create the quiz app
from core.models import Follower
from .models import Quiz, Category, FourChoicesQuestion, TrueOrFalseQuestion
from core.models import Streak, Profile
from ads.models import PostAd
# from draft.models import DraftQuiz
from comment.models import QuizComment, Comment

# Utilities
from random import shuffle
from .utils import sortKey, quizRandomCoin, randomChoice

import decimal
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
from django.contrib.auth.mixins import LoginRequiredMixin
# make sure you add the question mode herein

# xhtml2pdf
from diary.models import Diary


"""
Create a page for only users that are not logged in to taste the fun of the app before signing up
"""

class GeneratePDF(LoginRequiredMixin, View):

    def get(self, request, quiz_id, **kwargs):
        user = self.request.user
        template = get_template('quiz/takequiz.html')
        quiz = get_object_or_404(Quiz, id=quiz_id)

        preQuestions = []
        preQuestions += quiz.fourChoicesQuestions.all()
        preQuestions += quiz.trueOrFalseQuestions.all()
        questionsList = []
        for question in preQuestions:
            questionsList.append(tuple((question.index, question)))


        questionsList.sort(key=sortKey)
        questions = []
        for question in questionsList:
            questions.append(question[1])
        if request.method == 'GET':
            if quiz.shuffleable == True:
                shuffle(questions)

        context = {
            'quiz': quiz,
            'questions': questions,
        }

        html = template.render(context)
        pdf = render_to_pdf('quiz/quizPdf.html', context)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"quiz_{quiz.title}.pdf"
            # content = f"inline; filename={filename}"
            content = f"attachment; filename={filename}"
            response['Content-Disposition'] = content

            return response
        return HttpResponse("Not Found!")



# the details of a quiz

def QuizDetail(request, quiz_id, *args, **kwargs):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
    if not user.is_authenticated:
        code = str(kwargs.get('ref_code'))
        print('This is the code', code)
        try:
            profile = get_object_or_404(Profile, code=code)
            profile.coins += 50
            profile.refercount += 1
            profile.save()
            print('This is the profile', profile)
        except:
            pass    

    postAd = PostAd.objects.all()
    postAd = randomChoice(postAd)
        
    context = {
        'quiz': quiz,
        'user': user,
        'postAd': postAd,
        'profile': profile or 'None',
    }


    return render(request, 'quiz/quizdetail.html', context)

@login_required(redirect_field_name='next', login_url='account_login')
def CreateObject(request):
    return render(request, 'quiz/create.html')


"""
Add all the documentation here
"""
# the quiz list view
@login_required(redirect_field_name='next', login_url='account_login')
def QuizList(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    search_input= request.GET.get('search-area') or ''
    if search_input:
        quizzes = Quiz.objects.none()
        search = search_input.strip()
        search = search.split()
        for search_word in search:
            lookup = Q(title__icontains=search_word) | Q(description__icontains=search_word)
            quizzes |= Quiz.objects.filter(lookup).distinct().order_by('-likes', '-attempts')
    else:
        quizzes = Quiz.objects.all()
        # for category in profile.categories.all():
        # lookup = Q(categories in profile.categories.all()) | Q(average_score__gte=(100 - profile.avgScore)) 
        # quizzes = Quiz.objects.filter(lookup).distinct().order_by('-likes', '-attempts')

    """
    quizzes = random.choices(quizzes, k=200)
    """
    # add split method

    # you can add the .exclude method to the queryset
    


    # quizzes.insert(0, ad)
    print('okay')
    # create pagination
    p = Paginator(quizzes, 10)
    page = request.GET.get('page')
    quizzes = p.get_page(page)

    context={

        'search_input': search_input,
        'page_obj': quizzes,
        'profile': profile,
        'nav': 'quizzes',
    }


    return render(request, 'quiz/quizzes_list.html', context)



@login_required(redirect_field_name='next', login_url='account_login')
def FollowerQuizList(request):
    user = request.user
    follow = Follower.objects.get(user=user)
    profile = Profile.objects.get(user=user)
    quizzes = Quiz.objects.none()
    # add more abstraction for efficiency
    for following in follow.following.all():
        quizzes |= Quiz.objects.filter(user=following)

    # create pagination
    p = Paginator(quizzes, 10)
    page = request.GET.get('page')
    quizzes = p.get_page(page)

    context={
        'page_obj': quizzes,
        'nav': 'following-quizzes',
        'profile': profile,
    }


    return render(request, 'quiz/quizzes_list.html', context)





@login_required(redirect_field_name='next', login_url='account_login')
def MyQuizList(request):
    user = request.user
    quizzes = Quiz.objects.filter(user=user)
    # create pagination
    p = Paginator(quizzes, 10)
    page = request.GET.get('page')
    quizzes = p.get_page(page)

    context={
        'page_obj': quizzes,
        'nav': 'my-quizzes',
    }


    return render(request, 'quiz/quizzes_list.html', context)

"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def PostLike(request):
    user = request.user
    if request.method == 'POST':
        print(request)
        quiz_id = request.POST.get('quiz_id')
        quiz = Quiz.objects.get(id=quiz_id)
        profile = Profile.objects.get(user=quiz.user)
        print(quiz)


        if user in quiz.likes.all():
            quiz.likes.remove(user)
            profile.likes -= 1

            print('removed user')
        else:
            quiz.likes.add(user)
            profile.likes += 1
            print('added user')
        quiz.save()
        profile.save()


    return redirect('quiz:quizzes')

"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def QuizCreate(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = NewQuizForm()
    print(form)
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            description=form.cleaned_data.get('description')
            duration = form.cleaned_data.get('duration')

            quiz = Quiz.objects.create(user=user, title=title, description=description, duration=duration)
            profile.quizzes += 1
            profile.save()
            # return redirect('quiz:new-question', quiz_id=quiz.id)
            return redirect('quiz:category-create', quiz_id=quiz.id)
    
    context= {
        'form': form,
    }

    return render(request, 'quiz/quizCreate.html', context)






"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def QuizUpdate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if user != quiz.user:
        return HttpResponseForbidden()
    
    form = NewQuizForm(instance=quiz)
    if request.method == 'POST':
        form = NewQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()


            return redirect('quiz:category-create', quiz_id=quiz.id)
    
    context= {
        'form': form,
        'quiz': quiz,
    }

    return render(request, 'quiz/quizCreate.html', context)






# create the quiz delete view
@login_required(redirect_field_name='next', login_url='account_login')
def DeleteQuiz(request, quiz_id):
    user = request.user
    profile = Profile.objects.get(user=user)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        profile.quizzes -= 1
        profile.save()
        quiz.delete()


        return redirect('quiz:quizzes')
    
    return render(request, 'quiz/quiz_delete.html', {'obj': quiz})


 


"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def QuestionCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)

    context={
        'quiz': quiz,
    }
    
    return render(request, 'quiz/newquestion.html', context)





@login_required(redirect_field_name='next', login_url='account_login')
def FourChoicesQuestionCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form = NewFourChoicesQuestionForm()
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST)
        if form.is_valid():
            question_text= form.cleaned_data.get('question_text')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            answer3=form.cleaned_data.get('answer3')
            answer4=form.cleaned_data.get('answer4')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration')


            question = FourChoicesQuestion.objects.create(user=user, question_text=question_text,
            answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4,
            correct=correct, points=points, duration=duration)

            quiz.fourChoicesQuestions.add(question)
            quiz.lastQuestionIndex += 1
            quiz.questionLength += 1
            quiz.totalScore += question.points
            quiz.save()
            question.index = quiz.lastQuestionIndex
            question.save()

            return redirect('quiz:new-question', quiz_id=quiz.id)
    
    context= {
        'fourChoicesForm': form,
    }

    return render(request, 'quiz/fourChoicesQuestionCreate.html', context)


#



"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def TrueOrFalseQuestionCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form = NewTrueOrFalseQuestionForm()
    if request.method == 'POST':
        form = NewTrueOrFalseQuestionForm(request.POST)
        if form.is_valid():
            question_text= form.cleaned_data.get('question_text')
            answer1=form.cleaned_data.get('answer1')
            answer2=form.cleaned_data.get('answer2')
            correct=form.cleaned_data.get('correct')
            points=form.cleaned_data.get('points')
            duration=form.cleaned_data.get('duration')


            question = TrueOrFalseQuestion.objects.create(user=user, question_text=question_text,
            correct=correct, points=points,
            duration=duration)

            quiz.trueOrFalseQuestions.add(question)
            quiz.lastQuestionIndex += 1
            quiz.questionLength += 1
            quiz.totalScore += question.points
            quiz.save()
            question.index = quiz.lastQuestionIndex
            question.save()
            return redirect('quiz:new-question', quiz_id=quiz.id)
    
    context= {
        'trueOrFalseForm': form,
    }

    return render(request, 'quiz/trueOrFalseQuestionCreate.html', context)





"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def FourChoicesQuestionUpdate(request, quiz_id, question_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(FourChoicesQuestion, id=question_id)
    
    fourChoicesForm = NewFourChoicesQuestionForm(instance=question)
    if request.method == 'POST':

        form = NewFourChoicesQuestionForm(request.POST, instance=question)
        if form.is_valid():
            quiz.totalScore -= question.points
            instance = form.save()
            quiz.totalScore += instance.points
            quiz.save()
            return redirect('quiz:quiz-detail', quiz_id=quiz.id)
    
    context= {
        'fourChoicesForm': fourChoicesForm,
    }

    return render(request, 'quiz/fourChoicesQuestionCreate.html', context)


@login_required(redirect_field_name='next', login_url='account_login')
def TrueOrFalseQuestionUpdate(request, quiz_id, question_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(TrueOrFalseQuestion, id=question_id)
    ftrueOrFalseForm = NewTrueOrFalseQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST, instance=question)
        if form.is_valid():
            quiz.totalScore -= question.points
            instance = form.save()
            quiz.totalScore += instance.points
            quiz.save()
            return redirect('quiz:quiz-detail', quiz_id=quiz.id)
    
    context= {
        'trueOrFalseForm': trueOrFalseForm,
    }

    return render(request, 'quiz/trueOrFalseQuestionCreate.html', context)




"""
Add all the documentation here
"""
@login_required(redirect_field_name='next', login_url='account_login')
def CategoryCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form = NewCategoryForm()
    categories = Category.objects.all()

    title = request.GET.get('newCategory') or ''
    title = title.strip()
    title = title.split(' ')
    title = '-'.join(title)
    if title:

        if quiz.categories.all().count() < 3:
            category = None
            try:
                category = Category.objects.get(title__iexact=title)
            except:
                pass

            if category:
                if category not in quiz.categories.all():
                    quiz.categories.add(category)
                    quiz.save()  
                    messages.success(request, f"{category} has been added!")      
                else:
                    messages.warning(request, "This category has already been added!")      
            # return a message that it is already created
            else:
                newCategory = Category.objects.create(registered_by=user, title=title)
                quiz.categories.add(newCategory)
                quiz.save()
                messages.success(request, f"{newCategory} has been added!")      



    # create pagination
    quizCategories = quiz.categories.all()
    addedCategories = request.GET.getlist('addedCategories') or ''
    if addedCategories:
        
        for category in quizCategories:
            if category not in addedCategories:
                quiz.categories.remove(category)

        for cart in addedCategories:
            if quiz.categories.all().count() < 3:
                category = Category.objects.get(title__iexact=cart) or None
                if category:
                    if category not in quiz.categories.all():
                        quiz.categories.add(category)
                        quiz.save()

        
    quizCategories = quiz.categories.all()


    context= {
        'page_obj': categories,
        'quizCategories' : quizCategories,
        'quiz': quiz,

    }

    return render(request, 'quiz/categoryCreate.html', context)




@login_required(redirect_field_name='next' ,login_url='account_login')
def DeleteQuestion(request,quiz_id, question_form, question_id):
    user =request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if question_form == 'fourChoices':
        question = FourChoicesQuestion.objects.get(id=question_id)
    elif question_form == 'trueOrFalse':
        question = TrueOrFalseQuestion.objects.get(id=question_id)
    if request.method == 'POST':
        quiz.questionLength -= 1
        quiz.totalScore -= question.points
        question.delete()
        messages.success(request, "You've successfully delete a question!")
        return redirect('profile')

    context={
        'obj': question,
    }

    return render(request, 'question/delete.html', context)




# the real test view
"""
Add all the documentation here
"""
def TakeQuiz(request, quiz_id):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)

    quiz = get_object_or_404(Quiz, id=quiz_id)

    preQuestions = []
    preQuestions += quiz.fourChoicesQuestions.all()
    preQuestions += quiz.trueOrFalseQuestions.all()
    questionsList = []
    for question in preQuestions:
        questionsList.append(tuple((question.index, question)))


    questionsList.sort(key=sortKey)
    questions = []
    for question in questionsList:
        questions.append(question[1])
    
    if quiz.shuffleable == True:
        shuffle(questions)
    if user.is_authenticated:
        profile.coins -= 1
        profile.save()

    """
    Create a logic to take care of accounts with less than 1 coins
    Add reward of 1,2,2,2,2,3,3,3,4,4,5
    """


    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz/takequiz.html', context)







"""
create a lot of utilities for employees, like the one that will resolve the response of takenquiz
Give the full report of the quiz to the taker
all questions, questions taken, questions skipped, questions correct, questions wrong will be stored in your attempt model
handle all the questions that are not taken
all the report will be submitted to the creator of the questions too.
The total score should be adjusted whenever the creator the quiz updates the points of a question
"""
#totalScore, questionLength

def SubmitQuiz(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    postAd = PostAd.objects.all()
    postAd = randomChoice(postAd)
        
    if user.is_authenticated:
        profile = get_object_or_404(Profile, user=user)
    
    
    if request.method == 'POST':
        score = 0
        postAd = PostAd.objects.all()
        postAd = randomChoice(postAd)
        if user.is_authenticated:
            streak = Streak.objects.get(profile=profile)

        points = request.POST.get('points')
        answers = request.POST.getlist('answer')
        questionsList = []
  
        for answer in answers:
            combination = tuple(answer.split('|'))
            
            if combination[0] == 'fourChoicesQuestion':
                question = FourChoicesQuestion.objects.get(id=combination[1])
                pos = combination[2]
                answer = question.getAnswer(pos)
                questionsList.append((question, answer))
                if question.correct == combination[2]:
                    score += question.points
                    if user.is_authenticated:
                        if quiz.user != profile.user:
                            streak.validateStreak()
                            streak.save()

                    
            elif combination[0] == 'trueOrFalseQuestion':
                question = TrueOrFalseQuestion.objects.get(id=combination[1])
                answer = question.getAnswer(combination[2])
                questionsList.append((question, answer))
                if question.correct == answer:
                    score += question.points
                    if user.is_authenticated:
                        if quiz.user != profile.user:
                            streak.validateStreak()
                            streak.save()



        total_score = quiz.totalScore
        user_score = score
        if user.is_authenticated:
            if user_score > 0:
                quiz.attempts += 1
                user_avg_score = (user_score/total_score) * 100
                if user_avg_score >= 60:
                    if quiz.user != profile.user:
                        creator = Profile.objects.get(user=quiz.user)
                        for category in quiz.categories.all():
                            if category not in profile.categories.all():
                                if profile.categories.all().count() > 99:
                                    removed = profile.categories.first()
                                    profile.categories.remove(removed)
                                profile.categories.add(category)

                    
                        value = quizRandomCoin()
                        profile.coins += value
                        profile.save()
                        creator.coins += 1
                        creator.save()
                        messages.success(request, f"You've won {value} coins!")

                quiz.gross_average_score += user_avg_score
                quiz.average_score = quiz.gross_average_score / quiz.attempts 
                quiz.save()
                if quiz not in profile.quizTaken.all():
                    if profile.quizTaken.all().count() > 99:
                        removed = profile.quizTaken.first()
                        profile.quizTaken.remove(removed)
                    profile.quizTaken.add(quiz)
                profile.quizAttempts += 1
                profile.quizAvgScore = decimal.Decimal(round(((profile.quizAvgScore * (profile.quizAttempts - 1) + decimal.Decimal(user_avg_score)) / profile.quizAttempts), 1))

                profile.save()
            else:
                
                messages.error(request, "You didn't answer any question.")
                return redirect('quiz:take-quiz', quiz_id = quiz.id)
        else:
            if score > 0:
                user_score = score
            else:
                messages.error(request, "You didn't answer any question.")
                return redirect('question:answer-question')

                   
        context = {
            'quiz': quiz,
            'user_score': user_score,
            'total_score': total_score,
            'questionsList': questionsList,
            'postAd': postAd,
        }

        
    return render(request, 'quiz/submitQuiz.html', context)


