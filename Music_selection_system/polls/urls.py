from django.urls import path
from . import views
from .views import register_view


app_name = 'polls'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('register/', register_view, name='register'),
]

