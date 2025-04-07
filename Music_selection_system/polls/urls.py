from django.urls import path
from . import views



app_name = 'polls'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]




