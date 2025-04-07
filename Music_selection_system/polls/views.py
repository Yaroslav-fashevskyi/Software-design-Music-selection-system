from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth import login
from .forms import UserRegistrationForm

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
            return redirect('http://127.0.0.1:8000/polls/')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


# Create your views here.
