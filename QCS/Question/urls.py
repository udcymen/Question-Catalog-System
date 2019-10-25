from django.urls import path

from . import views

urlpatterns = [
    path('', views.detail, name='detail'),
    path('index', views.home, name='home'),
    # path('', views.index, name='index'),
    # path('index', views.question_index, name='question_index'),
    # # path('question/', views.index, name='index'),
    # # path('question/<str:id>', views.detail, name='detail'),
    # path('question/<int:question_id>', views.get_question_by_id, name='get_question_by_id'),
    # path('api/questions', views.api_questions, name='api_questions'),
    # path('api/question/<int:question_id>', views.api_question_id, name='api_question_id'),
]