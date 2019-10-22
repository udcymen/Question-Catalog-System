from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Course(models.Model):
    # Primary Key
    id = models.PositiveSmallIntegerField(primary_key=True)

    # Regular Fields
    name = models.CharField(max_length=256)

    def __str__(self):
        return "CISC" + str(self.id) + ": " + str(self.name)


class Topic(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)

    # Regular Fields
    topic = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id) + ": " + str(self.topic)


class Type(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)

    # Regular Fields
    type = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id) + ": " + str(self.type)


class User(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)

    # Regular Fields
    user_name = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    # TODO Add account validation period

    def __str__(self):
        return self.user_name + ": " + self.email


class ChangeLog(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)

    # Foreign Keys
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Regular Fields
    change_set = models.CharField(max_length=256)
    previous_version = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "Modified by " + str(self.user) + " at " + str(self.date)


class Question(models.Model):
    class Meta:
        unique_together = (("course", "name"),)

    # Primary Key
    id = models.AutoField(primary_key=True)

    # Foreign Keys
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic)
    forked_from = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)  # Can be Null
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    last_editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_editor')

    # Regular Fields
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    instruction = models.CharField(max_length=256)
    difficulty = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
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
        return str(self.course) + " " + str(self.name)


class Submission(models.Model):
    # Primary Key
    id = models.PositiveIntegerField(primary_key=True)

    # Foreign Keys
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Regular Fields
    student_code = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)
    score = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    feedback = models.CharField(max_length=256)
    input = models.CharField(max_length=256)
    output = models.CharField(max_length=256)
    detail = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id) + " Links to " + str(self.id)
