from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Question


def index(request):
    question_list = Question.objects.order_by('create_date')[:5]
    context = {
        'question_list': question_list,
    }
    return render(request, 'question.html', context)


def create(request):
    return render(request, 'create_question.html')


def detail(request):
    return HttpResponse("Hello")


def api_questions(request):
    return HttpResponse(serializers.serialize('json', list(Question.objects.all())))


def api_question_id(request, question_id):
    return HttpResponse(serializers.serialize('json', [Question.objects.get(pk=question_id)]))
