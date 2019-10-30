from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Question, Course
from django.forms import ModelForm
import re


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
            Question.objects.save()
            return HttpResponse('TODO')
        else:
            return HttpResponse('You are not logged in', status=401)


@require_http_methods(["GET", "POST", "DELETE"])
def question_detail(request, question_ref):
    if request.method == "GET":
        question = get_question(question_ref)
        form = QuestionForm(instance=question)
        return render(request, 'question_detail.html', {'form': form})

    elif request.method == "POST":
        # TODO Update
        if request.user.is_authenticated:
            return HttpResponse("TBD")
            
    elif request.method == "DELETE":
        # TODO Delete
        if request.user.is_authenticated:
            return HttpResponse("TBD")


def get_question(question_ref):
    if isinstance(question_ref, int):
        question = get_object_or_404(Question, pk=question_ref)
    else:
        question_name_list = question_ref.split('-')
        roman_numeral = re.search('^(?=[MDCLXVI])M*(C[MD]|D?C*)(X[CL]|L?X*)(I[XV]|V?I*)$', question_name_list[-1], re.IGNORECASE)
        if roman_numeral:
            question_name_list.pop()
        question_name = " ".join([s.capitalize() for s in question_name_list])
        if roman_numeral:
            question_name += (" " + roman_numeral.string.upper())
        question = get_object_or_404(Question, name=question_name)
    return question


