# from django.shortcuts import render

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseForbidden

# # function based views
# from django.views.generic.edit import FormView
# from django.urls import reverse_lazy

# from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import login


# # Create your views here.

# class RegisterPage(FormView):
#     template_name = 'quiz/register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('quiz:quizzes')
    
#     def form_valid(self, form):
#         user = form.save()
#         # logs the user in after registration
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('quiz:quizzes')
#         return super(RegisterPage, self).get(*args, **kwargs)



# class CustomLoginView(LoginView):
#     template_name = 'quiz/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
    
#     def get_success_url(self):
#         return reverse_lazy('quiz:quizzes')
