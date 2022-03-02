
# important method to deal with models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.db.models import Q

# the forms for each model
from .forms import NewQuizForm, NewCategoryForm, NewFourChoicesQuestionForm, NewTrueOrFalseQuestionForm


# the models to be used to create the quiz app

from .models import Quiz, Category, FourChoicesQuestion, TrueOrFalseQuestion, Attempter, Attempt
from core.models import Streak, Profile
from analysis.models import UserPageCounter, PageCounter

# Utilities
from random import shuffle
from .utils import sortKey


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

# make sure you add the question mode herein

# xhtml2pdf
from diary.models import Diary


"""
Create a page for only users that are not logged in to taste the fun of the app before signing up
"""

@login_required(login_url='login')
class GeneratePDF(View):
    def get(self, request, quiz_id, *args, **kwargs):
        user = self.request.user
        # template = get_template('quiz/takequiz.html')
        template = get_template('diary/diary_list.html')

        quiz = get_object_or_404(Quiz, id=quiz_id)

        diaries = Diary.objects.filter(user=request.user)
        count = diaries.count()

        context={
        'diaries': diaries,
        'count': count,
        }


        # context = {
        #     'quiz': quiz,
        # }
        html = template.render(context)
        # pdf = render_to_pdf('quiz/takequiz.html', context)
        pdf = render_to_pdf('diary/diary_list.html', context)


        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"quiz_{quiz.title}.pdf"
            # content = f"inline; filename={filename}"
            content = f"attachment; filename={filename}"
            response['Content-Disposition'] = content
            pagecounter = PageCounter.objects.get(id=1)
            pagecounter.pdfDownload += 1
            pagecounter.save()

            userpagecounter = UserPageCounter.objects.get(user=user)
            userpagecounter.pdfDownload += 1
            userpagecounter.save()

            return response
        return HttpResponse("Not Found!")



# the details of a quiz
@login_required(login_url='login')

def QuizDetail(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)

    
    context = {
        'quiz': quiz,
        'user': user,
    }

    pagecounter = PageCounter.objects.get(id=1)
    pagecounter.quizDetailPage += 1
    pagecounter.save()

    userpagecounter = UserPageCounter.objects.get(user=user)
    userpagecounter.quizDetailPage += 1
    userpagecounter.save()

    return render(request, 'quiz/quizdetail.html', context)





"""
Add all the documentation here
"""
# the quiz list view
@login_required(login_url='login')
def QuizList(request):
    user = request.user
    quizzes = Quiz.objects.all()# shuffle with .order_by('?')
    # add split method

# you can add the .exclude method to the queryset
    search_input= request.GET.get('search-area') or ''
    if search_input:
        quizzes = Quiz.objects.none()
        search = search_input.strip()
        search = search.split()
        for search_word in search:
            lookup = Q(title__icontains=search_word) | Q(description__icontains=search_word)
            quizzes |= Quiz.objects.filter(lookup).distinct()



    # quizzes.insert(0, ad)

    # create pagination
    p = Paginator(quizzes, 100)
    page = request.GET.get('page')
    quizzes = p.get_page(page)

    context={
        'search_input': search_input,
        'page_obj': quizzes,
    }

    pagecounter = PageCounter.objects.get(id=1)
    pagecounter.quizListPage += 1
    pagecounter.save()

    userpagecounter = UserPageCounter.objects.get(user=user)
    userpagecounter.quizListPage += 1
    userpagecounter.save()

    return render(request, 'quiz/quizzes_list.html', context)




"""
Add all the documentation here
"""
@login_required(login_url='login')
def QuizCreate(request):
    user = request.user
    form = NewQuizForm()
    if request.method == 'POST':
        form = NewQuizForm(request.POST, request.FILES)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            description=form.cleaned_data.get('description')
            duration = form.cleaned_data.get('duration')

            quiz = Quiz.objects.create(user=user, title=title, description=description, duration=duration)
            pagecounter = PageCounter.objects.get(id=1)
            pagecounter.quizCreationPage += 1
            pagecounter.save()

            userpagecounter = UserPageCounter.objects.get(user=user)
            userpagecounter.quizCreationPage += 1
            userpagecounter.save()
            # return redirect('quiz:new-question', quiz_id=quiz.id)
            return redirect('quiz:category-create', quiz_id=quiz.id)
    
    context= {
        'form': form,
    }

    return render(request, 'quiz/quizCreate.html', context)






"""
Add all the documentation here
"""
@login_required(login_url='login')

def QuizUpdate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if user != quiz.user:
        return HttpResponseForbidden()
    
    form = NewQuizForm(instance=quiz)
    if request.method == 'POST':
        form = NewQuizForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            form.save()
            
            pagecounter = PageCounter.objects.get(id=1)
            pagecounter.quizUpdatePage += 1
            pagecounter.save()

            userpagecounter = UserPageCounter.objects.get(user=user)
            userpagecounter.quizUpdatePage += 1
            userpagecounter.save()

            return redirect('quiz:category-create', quiz_id=quiz.id)
    
    context= {
        'form': form,
        'quiz': quiz,
    }

    return render(request, 'quiz/quizCreate.html', context)






# create the quiz delete view
@login_required(login_url='login')
def DeleteQuiz(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        quiz.delete()

        
        pagecounter = PageCounter.objects.get(id=1)
        pagecounter.quizDeletePage += 1
        pagecounter.save()

        userpagecounter = UserPageCounter.objects.get(user=user)
        userpagecounter.quizDeletePage += 1
        userpagecounter.save()

        return redirect('quiz:quizzes')
    
    return render(request, 'quiz/quiz_delete.html', {'obj': quiz})





"""
Add all the documentation here
"""
@login_required(login_url='login')

def QuestionCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)

    context={
        'quiz': quiz,
    }
    
    return render(request, 'quiz/newquestion.html', context)





@login_required(login_url='login')

def FourChoicesQuestionCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form = NewFourChoicesQuestionForm()
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST, request.FILES)
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
@login_required(login_url='login')

def TrueOrFalseQuestionCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form = NewTrueOrFalseQuestionForm()
    if request.method == 'POST':
        form = NewTrueOrFalseQuestionForm(request.POST, request.FILES)
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
@login_required(login_url='login')

def FourChoicesQuestionUpdate(request, quiz_id, question_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(FourChoicesQuestion, id=question_id)
    form = NewFourChoicesQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('quiz:quiz-detail', quiz_id=quiz.id)
    
    context= {
        'form': form,
    }

    return render(request, 'quiz/fourChoicesQuestionCreate.html', context)


@login_required(login_url='login')

def TrueOrFalseQuestionUpdate(request, quiz_id, question_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(TrueOrFalseQuestion, id=question_id)
    form = NewTrueOrFalseQuestionForm(instance=question)
    if request.method == 'POST':
        form = NewFourChoicesQuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('quiz:quiz-detail', quiz_id=quiz.id)
    
    context= {
        'form': form,
    }

    return render(request, 'quiz/trueOrFalseQuestionCreate.html', context)



"""
Add all the documentation here
"""
@login_required(login_url='login')

def CategoryCreate(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form = NewCategoryForm()
    categories = Category.objects.all()

    title = request.GET.get('newCategory') or ''
    if title:

        try:
            Category.objects.get(title__icontains=title)
            # return a message that it is already created
        except:
            newCategory = Category.objects.create(registered_by=user, title=title)
            quiz.categories.add(newCategory)
            quiz.save()


    # create pagination
    quizCategories = quiz.categories.all()
    addedCategories = request.GET.getlist('addedCategories') or ''
    print(addedCategories)
    print(quizCategories)
    if addedCategories:
        
        for category in quizCategories:
            if category not in addedCategories:
                quiz.categories.remove(category)

        for category in addedCategories:
            category = Category.objects.get(title__icontains=category)
            if category is not None:
                if category not in quiz.categories.all():
                    quiz.categories.add(category)
                    quiz.save()


    context= {
        'page_obj': categories,
        'quiz': quiz,

    }

    return render(request, 'quiz/categoryCreate.html', context)



# the real test view
"""
Add all the documentation here
"""
@login_required(login_url='login')

def TakeQuiz(request, quiz_id):
    user = request.user
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


    pagecounter = PageCounter.objects.get(id=1)
    pagecounter.quizTakenPage += 1
    pagecounter.save()

    userpagecounter = UserPageCounter.objects.get(user=user)
    userpagecounter.quizTakenPage += 1
    userpagecounter.save()

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

@login_required(login_url='login')
def SubmitQuiz(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    profile = get_object_or_404(Profile, user=user)
    




    if request.method == 'POST':
        streak = Streak.objects.get(profile=profile)

        points = request.POST.get('points')
        answers = request.POST.getlist('answer')
        attempter = Attempter.objects.create(user=user, quiz=quiz, score=0)
        questionsList = []
  
        for answer in answers:
            combination = tuple(answer.split('|'))
            
            if combination[0] == 'fourChoicesQuestion':
                question = FourChoicesQuestion.objects.get(id=combination[1])
                pos = combination[2]
                answer = question.getAnswer(pos)
                questionsList.append((question, answer))
                if question.correct == combination[2]:
                    attempter.score += question.points
                    attempter.save()
                    streak.validateStreak()
                    streak.save()



            elif combination[0] == 'trueOrFalseQuestion':
                question = TrueOrFalseQuestion.objects.get(id=combination[1])
                answer = question.getAnswer(combination[2])
                questionsList.append((question, answer))
                if question.correct.lower() == answer.lower():
                    print('The answer is correct!')
                    attempter.score += question.points
                    attempter.save()
                    streak.validateStreak()
                    streak.save()
                    # try to remove the save method


        user_score = attempter.score
        total_score = quiz.totalScore

        if user_score > 0:
            quiz.attempts += 1
            quiz.gross_average_score += (user_score/total_score) * 100
            quiz.average_score = quiz.gross_average_score / quiz.attempts 
            quiz.save()
            pagecounter = PageCounter.objects.get(id=1)
            pagecounter.quizSubmitPage += 1
            pagecounter.save()

            userpagecounter = UserPageCounter.objects.get(user=user)
            userpagecounter.quizSubmitPage += 1
            userpagecounter.save()

        else:
            
            # messages.error(request, "You didn't answer any question.")
            return redirect('take-quiz', quiz_id = quiz.id)

                   

        context = {
            'quiz': quiz,
            'user_score': user_score,
            'total_score': total_score,
            'questionsList': questionsList,

        }

    return render(request, 'quiz/submitQuiz.html', context)