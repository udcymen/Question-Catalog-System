from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
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

    
def detail_id(request, question_id):
    if request.method == "GET":
        question = get_object_or_404(Question, pk=question_id)
        return HttpResponse("You're looking at question %s." % question)

    elif request.method == "POST":
        # TODO Update
        if request.user.is_authenticated():
            return HttpResponse("TBD")
            
    elif request.method == "DELETE":
        # TODO Delete
        if request.user.is_authenticated():
            return HttpResponse("TBD")

def detail_name(request, question_name):
    if "-" in question_name and question_name.islower():
        question_name = " ".join([s.capitalize() for s in question_name.split("-")])

    if request.method == "GET":
        question = get_object_or_404(Question, name=question_name)
        return HttpResponse("You're looking at question %s." % question)

    elif request.method == "POST":
        # TODO Update
        if request.user.is_authenticated():
            return HttpResponse("TBD")
            
    elif request.method == "DELETE":
        # TODO Delete
        if request.user.is_authenticated():
            return HttpResponse("TBD")
