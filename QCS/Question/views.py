from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question
from django.views.generic.base import TemplateView

def home(request):
    return TemplateView.as_view(template_name='home.html')

def detail(request):
    # Get Latest Ten Questions
    if request.method == "GET":
        question_list = Question.objects.order_by('create_date')[:10]
        context = {
            'question_list': question_list,
        }
        return render(request, 'question.html', context)

    elif request.method == "PUT":
        # TODO Create
        if request.user.is_authenticated():
            return render(request, 'create_question.html')

    
def detail_Id(request, question_id):

    if request.user.is_authenticated():
        if request.method == "GET":
            question = get_object_or_404(Question, pk=question_id)
            return HttpResponse(response % question)
        elif request.method == "POST":
            # TODO Update
            if request.user.is_authenticated():
                question = "ha"
            return HttpResponse("TBD")

        elif request.method == "DELETE":
            # TODO Delete
            return HttpResponse("TBD")
