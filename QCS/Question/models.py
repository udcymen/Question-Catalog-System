from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime

class Course(models.Model):
    class Meta:
        unique_together = [['year', 'semester', 'level']]


    # Regular Fields
    name = models.CharField(max_length=256)
    level = models.PositiveSmallIntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(999)])
    year = models.PositiveSmallIntegerField(default=datetime.datetime.now().year, validators=[MinValueValidator(1000), MaxValueValidator(9999)])

    # Semester Choice - ENUM
    FALL = 'FA'
    WINTER = 'WI'
    SPRING = 'SP'
    SUMMER = 'SU'
    SEMESTER = [
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer')
    ]
    semester = models.CharField(
        max_length=2,
        choices=SEMESTER,
        default=FALL
    )

    # Foreign Keys
    #   Non-Nullable
    professor = models.ManyToManyField(User, related_name='professor')
    #   Nullable
    teaching_assitant = models.ManyToManyField(User, related_name='teaching_assitant', blank=True)
    students = models.ManyToManyField(User, related_name='student', blank=True)
    

    def __str__(self):
        return " ".join([str(self.year), self.get_semester_display(), "CISC" + str(self.level), self.name])


class Topic(models.Model):
    # Regular Fields
    topic = models.CharField(max_length=256)

    def __str__(self):
        return self.topic


class QuestionType(models.Model):
    # Regular Fields
    type = models.CharField(max_length=256)

    def __str__(self):
        return self.type


# class UserProfile(models.Model):
    # Foreign Keys
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class QuestionChangeLog(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    
    # Regular Fields
    change_set = models.CharField(max_length=256)
    previous_version = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.question) + ": Version " + str(self.previous_version)


class Question(models.Model):
    # Foreign Keys
    #   Nullable
    course = models.ManyToManyField(Course, blank=True)
    topic = models.ManyToManyField(Topic, blank=True)
    forked_from = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    #   Non-Nullable
    type = models.ManyToManyField(QuestionType)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    last_editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_editor')

    # Regular Fields
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    instruction = models.CharField(max_length=256)
    difficulty = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)
    version = models.PositiveIntegerField(editable=False)
    student_test = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.version = 1
        else:
            self.version += 1
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Submission(models.Model):
    # Foreign Keys
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Regular Fields
    name = models.CharField(max_length=256)
    student_code = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)
    score = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    feedback = models.CharField(max_length=256)
    parameter = models.CharField(max_length=256)
    output = models.CharField(max_length=256)
    detail = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.name

