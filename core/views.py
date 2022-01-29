from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# function based views
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from django.contrib import messages
# # Create your views here.
# messages.error, warning, success, info, debug
def CustomLoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quiz:quizzes')
        else:
            messages.error(request, 'Username or password does not exist')


    context={

    }
    return render(request, 'core/login.html',context)


# user registration form
class RegisterPage(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('quiz:quizzes')

    def form_invalid(self, form):
        messages.error(self.request, "Your password can't be too similar to your other personal information.")
        messages.error(self.request, "Your password must contain at least 8 characters.")
        messages.error(self.request, "Your password can't be a commonly used password.")
        messages.error(self.request, "Your password can't be entirely numeric.")
        return super(RegisterPage, self).form_invalid(form)

        
    def form_valid(self, form):
        user = form.save()
        # logs the user in after registration
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, 'Username or password does not exist')
        return super(RegisterPage, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('quiz:quizzes')
        return super(RegisterPage, self).get(*args, **kwargs)

