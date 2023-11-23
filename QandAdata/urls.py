# QandAdata/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('questions/', views.QuestionListView.as_view(), name='question-list'),
    path('answers/', views.AnswerListView.as_view(), name='answer-list'),
]
