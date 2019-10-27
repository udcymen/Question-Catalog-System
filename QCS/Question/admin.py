from django.contrib import admin
from .models import *

# Register your models here.
root_admin = [Course, Topic, QuestionType, Question, Submission, QuestionChangeLog]
admin.site.register(root_admin)
