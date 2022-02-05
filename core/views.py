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

from .models import Profile
from .forms import ProfileCreationForm
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
            messages.success(self.request, f"Welcome to the resersi network!")
            messages.success(self.request, f"Count yourself lucky to join the community of the people that are going to change world.")
            messages.success(self.request, f"Create or take any quiz.")
            login(self.request, user)
        else:
            messages.error(self.request, 'Username or password does not exist')
        return super(RegisterPage, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(self.request, f"{self.request.user.username}, you've already registered!")
            return redirect('quiz:quizzes')
        return super(RegisterPage, self).get(*args, **kwargs)



def ProfilePage(request):
    user = request.user
    if not user.is_authenticated:
        messages.warning(request, "Login to continue")
        return redirect('login')


    profile = get_object_or_404(Profile, user=user)

    context={
        'profile': profile,
    }

    return render(request, 'core/profile.html', context)



def ProfileCreationPage(request):
    user = request.user
    if not user.is_authenticated:
        messages.warning(self.request, "Login to continue")
        return redirect('login')

    profile = get_object_or_404(Profile, user=user)

    form = ProfileCreationForm(instance=profile)

    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"{user.username}, you have successfully edited your profile.")
            messages.info(request, f"{user.username}, did you know that the brain neurons die one after the other if they are idle?")
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'core/profile_form.html', context)









