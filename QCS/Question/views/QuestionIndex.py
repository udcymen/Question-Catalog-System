from django.shortcuts import render
from ..models.Question import Question
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET"])
def quetion_index(request):
    # Get Latest Ten Questions
    if request.method == "GET":
        question_list = Question.objects.order_by('create_date')[:10]
        return render(request, 'question-index.html', {'question_list': question_list})
