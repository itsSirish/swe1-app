import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question, Choice


# Create your tests here.
class BasicTestCase(TestCase):
    """
    Basic test case to ensure testing infrastructure is working.
    You can add more specific tests here later.
    """

    def test_basic_assertion(self):
        """Test that basic assertions work"""
        self.assertEqual(1 + 1, 2)

    def test_true_is_true(self):
        """Test that True is True"""
        self.assertTrue(True)

    def test_false_is_false(self):
        """Test that False is False"""
        self.assertFalse(False)


class QuestionModelTests(TestCase):
    """Tests for the Question model"""

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_question_str_method(self):
        """Test that the __str__ method returns the question text"""
        question = Question(question_text="What's up?")
        self.assertEqual(str(question), "What's up?")


class ChoiceModelTests(TestCase):
    """Tests for the Choice model"""

    def test_choice_str_method(self):
        """Test that the __str__ method returns the choice text"""
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        choice = Choice.objects.create(question=question, choice_text="Test choice")
        self.assertEqual(str(choice), "Test choice")

    def test_choice_default_votes(self):
        """Test that new choices have 0 votes by default"""
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        choice = Choice.objects.create(question=question, choice_text="Test choice")
        self.assertEqual(choice.votes, 0)


class QuestionIndexViewTests(TestCase):
    """Tests for the index view"""

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = Question.objects.create(
            question_text="Past question.", pub_date=timezone.now()
        )
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )


# Test Travis CI via PR
