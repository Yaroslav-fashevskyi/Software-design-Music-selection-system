from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Question
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
from .forms import UserLoginForm

def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'question_list.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Після успішного збереження, одразу авторизуємо користувача
            login(request, user)
            return redirect(reverse('question_list'))
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('question_list'))

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Повертаємо користувача на сторінку логіну (або на будь-яку іншу)

# Create your views here.
