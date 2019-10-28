from django.urls import path
from . import views

urlpatterns = [
    path('', views.quetion_index, name='quetion_index'),
    path('create', views.quetion_create, name='quetion_create'),
    path('<int:question_id>', views.quetion_detail_id, name='quetion_detail_id'),
    path('<str:question_name>', views.quetion_detail_name, name='quetion_detail_name'),
]