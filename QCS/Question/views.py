from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import *
from django.forms import ModelForm
from json import loads


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'type', 'author', 'name', 'description', 'instruction', 'difficulty']



@require_http_methods(["GET"])
def quetion_index(request):
    # Get Latest Ten Questions
    if request.method == "GET":
        question_list = Question.objects.order_by('create_date')[:10]
        return render(request, 'question_index.html', {'question_list': question_list})


@require_http_methods(["GET", "POST"])
def quetion_create(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # only professor can got to create question page
            if Course.objects.filter(professor=request.user).count() != 0:
                return render(request, 'question_create.html', {'form': QuestionForm()})
            else:
                return HttpResponse('You must be a professor of a course to create question', status=401)
        else:
            return HttpResponse('You are not logged in', status=401)
            
    elif request.method == "POST":
        # TODO Put Question into System
        if request.user.is_authenticated:
            question = Question.objects.create(
                type= QuestionType.objects.get(id =request.POST['type']),
                author= User.objects.get(id = request.POST['author']),
                last_editor = request.user,
                name=request.POST['name'],
                description=request.POST['description'],
                instruction=request.POST['instruction'], 
                difficulty=request.POST['difficulty']
            )
            for id in request.POST.getlist('topic'):
                question.topic.add(Topic.objects.get(id = id))
            return HttpResponse('TODO')
        else:
            return HttpResponse('You are not logged in', status=401)


@require_http_methods(["GET", "POST", "DELETE"])
def quetion_detail_id(request, question_id):
    if request.method == "GET":
        form = QuestionForm(instance=Question.objects.get(pk=question_id))
        return render(request, 'question_detail.html', {'form': form})

    elif request.method == "POST":
        # TODO Update
        if request.user.is_authenticated:
            return HttpResponse("TBD")
            
    elif request.method == "DELETE":
        # TODO Delete
        if request.user.is_authenticated:
            return HttpResponse("TBD")


@require_http_methods(["GET", "POST", "DELETE"])
def quetion_detail_name(request, question_name):
    if "-" in question_name and question_name.islower():
        question_name = " ".join([s.capitalize() for s in question_name.split("-")])

    if request.method == "GET":
        question = get_object_or_404(Question, name=question_name)
        return HttpResponse("You're looking at question %s." % question)

    elif request.method == "POST":
        # TODO Update
        if request.user.is_authenticated:
            return HttpResponse("TBD")
            
    elif request.method == "DELETE":
        # TODO Delete
        if request.user.is_authenticated:
            return HttpResponse("TBD")


