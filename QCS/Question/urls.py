from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('question/', views.index, name='index'),
    # path('question/<str:id>', views.detail, name='detail'),
    # path('question/create/', views.create, name='create_question')
    path('api/questions', views.api_questions, name='api_questions'),
    path('api/question/<int:question_id>', views.api_question_id, name='api_question_id'),
]