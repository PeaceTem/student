# from django.shortcuts import render, redirect, get_object_or_404
# from .models import DraftQuiz, DraftTrueOrFalseQuestion, DraftTrueOrFalseQuestion
# from .forms import NewDraftQuizForm, NewDraftFourChoicesQuestionForm, NewDraftTrueOrFalseQuestionForm

# from quiz.models import Quiz
# from django.contrib import messages

# from django.contrib.auth.decorators import login_required
# # Create your views here.



# @login_required(login_url='login')
# def DraftQuizList(request):
#     draftquizzes = DraftQuiz.objects.filter(user=request.user)

#     context={
#         'quizzes': draftquizzes,
#     }
#     return render(request, 'draft/draftquizlist.html', context)
# """
# Add all the documentation here
# """
# @login_required(login_url='login')
# def DraftQuizCreate(request):
#     user = request.user
#     form = NewDraftQuizForm()
#     if request.method == 'POST':
#         form = NewDraftQuizForm(request.POST, request.FILES)
#         if form.is_valid():
#             title= form.cleaned_data.get('title')
#             description=form.cleaned_data.get('description')
#             duration = form.cleaned_data.get('duration')

#             quiz = DraftQuiz.objects.create(user=user, title=title, description=description, duration=duration)
           
#             # return redirect('quiz:new-question', quiz_id=quiz.id)
#             return redirect('quiz:category-create', quiz_id=quiz.id)
    
#     context= {
#         'form': form,
#     }

#     return render(request, 'draft/quizCreate.html', context)





# """
# Add all the documentation here
# """
# @login_required(login_url='login')

# def CategoryCreate(request, quiz_id):
#     user = request.user
#     draftquiz = get_object_or_404(DraftQuiz, id=quiz_id)
#     form = NewCategoryForm()
#     categories = Category.objects.all()

#     title = request.GET.get('newCategory') or ''
#     if title:

#         try:
#             Category.objects.get(title__icontains=title)
#             # return a message that it is already created
#         except:
#             newCategory = Category.objects.create(registered_by=user, title=title)
#             draftquiz.categories.add(newCategory)
#             draftquiz.save()


#     # create pagination
#     quizCategories = draftquiz.categories.all()
#     addedCategories = request.GET.getlist('addedCategories') or ''
#     print(addedCategories)
#     print(quizCategories)
#     if addedCategories:
        
#         for category in quizCategories:
#             if category not in addedCategories:
#                 draftquiz.categories.remove(category)

#         for category in addedCategories:
#             category = Category.objects.get(title__icontains=category)
#             if category is not None:
#                 if category not in quiz.categories.all():
#                     draftquiz.categories.add(category)
#                     draftquiz.save()

#                     return JsonResponse({
#                         'page_obj': categories,
#                         'quizCategories' : quizCategories,
#                         'draftquiz': draftquiz,
#                     })
    
#     quizCategories = draftquiz.categories.all()


#     context= {
#         'page_obj': categories,
#         'quizCategories' : quizCategories,
#         'draftquiz': draftquiz,

#     }

#     return render(request, 'draft/categoryCreate.html', context)





# """
# If a user press go live, all the properties of the draft quiz will be converted to a live one and the draft quiz will be deleted.
# """
# @login_required(login_url='login')
# def ConvertDraftQuizToLive(request, quiz_id):
#     user = request.user
#     draftquiz = get_object_or_404(DraftQuiz, id=quiz_id)
#     try:
#         quiz = Quiz.objects.create(user=draftquiz.user, title=draftquiz.title, description=draftquiz.description,
#         duration=draftquiz.duration, lastQuestionIndex=draftquiz.lastQuestionIndex,
#         totalScore=draftquiz.totalScore, shuffleable=draftquiz.shuffleable, public=draftquiz.public,
#         thumbnail=draftquiz.thumbnail)
#         quiz.fourChoicesQuestions.add(*draftquiz.fourChoicesQuestions.all())
#         quiz.trueOrFalseQuestions.add(*draftquiz.trueOrFalseQuestions.all())
#         quiz.categories.add(*draftquiz.categories.all())
#         quiz.save()
#         draftquiz.delete()

#         messages.success(request, 'Quiz has been successfully created!')
#         return redirect('quiz:quiz-detail', quiz_id=quiz.id)


#     except:
#         messages.error(request, 'An Error Occurred!\nMake sure all fields are correctly filled!')
#         return redirect('draft:quiz-update', quiz_id=quiz_id)

#     return redirect('quiz:quiz-detail', quiz_id=quiz.id)



# """
# Add all the documentation here
# """
# @login_required(login_url='login')
# def DraftQuizUpdate(request, quiz_id):
#     user = request.user
#     quiz = get_object_or_404(DraftQuiz, id=quiz_id)
#     if user != quiz.user:
#         return HttpResponseForbidden()
    
#     form = NewDraftQuizForm(instance=quiz)
#     if request.method == 'POST':
#         form = NewDraftQuizForm(request.POST, request.FILES, instance=quiz)
#         if form.is_valid():
#             form.save()

#             return redirect('draft:category-create', quiz_id=quiz.id)
    
#     context= {
#         'form': form,
#         'quiz': quiz,
#     }

#     return render(request, 'draft/quizCreate.html', context)






# # create the quiz delete view
# @login_required(login_url='login')
# def DraftDeleteQuiz(request, quiz_id):
#     user = request.user
#     quiz = get_object_or_404(DraftQuiz, id=quiz_id)
#     if request.method == 'POST':
#         quiz.delete()

#         return redirect('quiz:quizzes')
    
#     return render(request, 'quiz/quiz_delete.html', {'obj': quiz})







# """
# Add all the documentation here
# """
# @login_required(login_url='login')

# def DraftQuestionCreate(request, quiz_id):
#     user = request.user
#     quiz = get_object_or_404(DraftQuiz, id=quiz_id)

#     context={
#         'quiz': quiz,
#     }
    
#     return render(request, 'quiz/newquestion.html', context)





# @login_required(login_url='login')

# def DraftFourChoicesQuestionCreate(request, quiz_id):
#     user = request.user
#     quiz = get_object_or_404(DraftQuiz, id=quiz_id)
#     form = NewFourChoicesQuestionForm()
#     if request.method == 'POST':
#         form = NewDraftFourChoicesQuestionForm(request.POST, request.FILES)
#         if form.is_valid():
#             question_text= form.cleaned_data.get('question_text')
#             answer1=form.cleaned_data.get('answer1')
#             answer2=form.cleaned_data.get('answer2')
#             answer3=form.cleaned_data.get('answer3')
#             answer4=form.cleaned_data.get('answer4')
#             correct=form.cleaned_data.get('correct')
#             points=form.cleaned_data.get('points')
#             duration=form.cleaned_data.get('duration')


#             question = DraftFourChoicesQuestion.objects.create(user=user, question_text=question_text,
#             answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4,
#             correct=correct, points=points, duration=duration)

#             quiz.fourChoicesQuestions.add(question)
#             quiz.lastQuestionIndex += 1
#             quiz.questionLength += 1
#             quiz.totalScore += question.points
#             quiz.save()
#             question.index = quiz.lastQuestionIndex
#             question.save()

#             return redirect('quiz:new-question', quiz_id=quiz.id)
    
#     context= {
#         'fourChoicesForm': form,
#     }

#     return render(request, 'quiz/fourChoicesQuestionCreate.html', context)


# #



# """
# Add all the documentation here
# """
# @login_required(login_url='login')

# def DraftTrueOrFalseQuestionCreate(request, quiz_id):
#     user = request.user
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     form = NewTrueOrFalseQuestionForm()
#     if request.method == 'POST':
#         form = NewTrueOrFalseQuestionForm(request.POST, request.FILES)
#         if form.is_valid():
#             question_text= form.cleaned_data.get('question_text')
#             answer1=form.cleaned_data.get('answer1')
#             answer2=form.cleaned_data.get('answer2')
#             correct=form.cleaned_data.get('correct')
#             points=form.cleaned_data.get('points')
#             duration=form.cleaned_data.get('duration')


#             question = TrueOrFalseQuestion.objects.create(user=user, question_text=question_text,
#             correct=correct, points=points,
#             duration=duration)

#             quiz.trueOrFalseQuestions.add(question)
#             quiz.lastQuestionIndex += 1
#             quiz.questionLength += 1
#             quiz.totalScore += question.points
#             quiz.save()
#             question.index = quiz.lastQuestionIndex
#             question.save()
#             return redirect('quiz:new-question', quiz_id=quiz.id)
    
#     context= {
#         'trueOrFalseForm': form,
#     }

#     return render(request, 'quiz/trueOrFalseQuestionCreate.html', context)





# """
# Add all the documentation here
# """
# @login_required(login_url='login')

# def DraftFourChoicesQuestionUpdate(request, quiz_id, question_id):
#     user = request.user
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     question = get_object_or_404(FourChoicesQuestion, id=question_id)
    
#     fourChoicesForm = NewFourChoicesQuestionForm(instance=question)
#     if request.method == 'POST':
#         quiz.totalScore -= question.points
#         quiz.save()
#         form = NewFourChoicesQuestionForm(request.POST, request.FILES, instance=question)
#         if form.is_valid():

#             instance = form.save()
#             quiz.totalScore += instance.points
#             quiz.save()

#             return redirect('quiz:quiz-detail', quiz_id=quiz.id)
    
#     context= {
#         'fourChoicesForm': fourChoicesForm,
#     }

#     return render(request, 'quiz/fourChoicesQuestionCreate.html', context)


# @login_required(login_url='login')

# def DraftTrueOrFalseQuestionUpdate(request, quiz_id, question_id):
#     user = request.user
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     question = get_object_or_404(TrueOrFalseQuestion, id=question_id)
#     ftrueOrFalseForm = NewTrueOrFalseQuestionForm(instance=question)
#     if request.method == 'POST':
#         quiz.totalScore -= question.points
#         quiz.save()
#         form = NewFourChoicesQuestionForm(request.POST, request.FILES, instance=question)
#         if form.is_valid():
#             form.save()
#             instance = form.save()
#             quiz.totalScore += instance.points
#             quiz.save()
#             return redirect('quiz:quiz-detail', quiz_id=quiz.id)
    
#     context= {
#         'trueOrFalseForm': trueOrFalseForm,
#     }

#     return render(request, 'quiz/trueOrFalseQuestionCreate.html', context)

