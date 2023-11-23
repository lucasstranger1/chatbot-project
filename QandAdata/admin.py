# QandAdata/admin.py

from django.contrib import admin
from .models import Category, Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'user_type')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'user_type')

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
