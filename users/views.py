from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import EdittUserForm, ChangedPasswordForm
from django.contrib.auth.views import PasswordChangeView


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('Home')
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form':form},)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
    else:
        return render(request, 'login.html', {},)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out successfully."))
    return redirect('Home')

class UserEditView(generic.UpdateView):
    form_class = EdittUserForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = ChangedPasswordForm
    success_url = reverse_lazy('Home')
    success_message = "Password changed successfully"