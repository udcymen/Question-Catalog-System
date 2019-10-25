from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question
from django.views.generic.base import TemplateView

def home(request):
    return TemplateView.as_view(template_name='home.html')

def detail(request):
    # if request.


def question_index(request):
    question_list = Question.objects.order_by('create_date')[:5]
    context = {
        'question_list': question_list,
    }
    return render(request, 'question.html', context)


def get_question_by_id(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    response = "You're looking at question %s."
    return HttpResponse(response % question)


def api_questions(request):
    return HttpResponse(serializers.serialize('json', list(Question.objects.all())))


def api_question_id(request, question_id):
    return HttpResponse(serializers.serialize('json', [Question.objects.get(pk=question_id)]))


def create(request):
    if request.user.is_authenticated():
        return render(request, 'create_question.html')
