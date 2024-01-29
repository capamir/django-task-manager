from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm
import random
from .models import  User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            User.objects.create_user(cd['phone'], cd['email'],
                                         cd['full_name'], cd['password'])

            messages.success(request, 'You registered succesfully', 'success')
            return redirect('projects:projects')
        return render(request, self.template_name, {'form':form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('projects:projects')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'info')
                return redirect('projects:projects')
            messages.error(request, 'phone or password is wrong', 'warning')
        return render(request, self.template_name, {'form':form})


class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'