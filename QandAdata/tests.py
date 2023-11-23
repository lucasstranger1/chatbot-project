# QandAdata/tests.py

from django.test import TestCase
from .models import Category, Question, Answer

class CategoryModelTest(TestCase):
    def test_str_representation(self):
        category = Category(name="HealthCare Givers")
        self.assertEqual(str(category), "HealthCare Givers")

class QuestionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="HealthCare Givers")
        self.question = Question.objects.create(
            category=self.category,
            question_text="What are the common health challenges faced by ASD kids?"
        )

    def test_str_representation(self):
        self.assertEqual(str(self.question), "What are the common health challenges faced by ASD kids?")

    def test_category_relation(self):
        self.assertEqual(self.question.category, self.category)

class AnswerModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="HealthCare Givers")
        self.question = Question.objects.create(
            category=self.category,
            question_text="What are the common health challenges faced by ASD kids?"
        )
        self.answer = Answer.objects.create(
            question=self.question,
            answer_text="ASD kids often face challenges in areas such as communication, sensory processing, and social interaction."
        )

    def test_str_representation(self):
        expected_str = "ASD kids often face challenges in areas such as communication, sensory processing, and social interaction."
        self.assertEqual(str(self.answer), expected_str)

    def test_question_relation(self):
        self.assertEqual(self.answer.question, self.question)
