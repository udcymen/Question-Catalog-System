from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail_id, name='detail_id'),
    path('<str:question_name>', views.detail_name, name='detail_name'),
]