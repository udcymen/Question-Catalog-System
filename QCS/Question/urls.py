from django.urls import path

from . import views

urlpatterns = [
    path('', views.detail, name='detail'),
    path('<int:question_id>', views.detail, name='detail'),
    path('index', views.home, name='home'),
]