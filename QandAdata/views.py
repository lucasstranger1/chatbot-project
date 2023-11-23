# QandAdata/views.py
from rest_framework import generics
from .models import Category, Question, Answer
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category', None)
        if category_id:
            return Question.objects.filter(category_id=category_id)
        return Question.objects.all()

class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question_id = self.request.query_params.get('question', None)
        category_id = self.request.query_params.get('category', None)

        queryset = Answer.objects.all()

        if question_id:
            queryset = queryset.filter(question_id=question_id)

        if category_id:
            # Assuming your Question model has a category field
            queryset = queryset.filter(question__category_id=category_id)

        return queryset
