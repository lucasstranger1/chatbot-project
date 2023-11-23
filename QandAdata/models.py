# models.py

from django.db import models
from django.contrib.auth.models import User

class UserType(models.TextChoices):
    HEALTHCARE_GIVER = 'healthcare_giver', 'Healthcare Giver'
    PARENT = 'parent', 'Parent'
    EDUCATOR = 'educator', 'Educator'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.TextField()
    user_type = models.CharField(max_length=20, choices=UserType.choices)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    user_type = models.CharField(max_length=20, choices=UserType.choices)

    def __str__(self):
        return self.answer_text
