# Create your tests here.
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import CustomUser, Student
from .models import Homework
from .validators import GradeValidator


class HomeworkTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='Student', email="student@example.com", password="password")
        self.student = Student.objects.create(user=self.user)

    def test_homework_save_updates_is_graded_and_avg_grade(self):
        homework = Homework.objects.create(student=self.student, title="Test Homework", description="Test content", grade=5)
        self.assertTrue(homework.is_graded)

        self.student.refresh_from_db()
        self.assertEqual(self.student.avg_grade, 5.0)

    def test_homework_save_without_grade(self):
        homework = Homework.objects.create(student=self.student, title="Test Homework", description="Test content", grade=None)

        self.assertFalse(homework.is_graded)
        self.student.refresh_from_db()
        self.assertEqual(self.student.avg_grade, 0.0)

    def test_homework_delete_updates_avg_grade(self):
        homework = Homework.objects.create(student=self.student, title="Test Homework", description="Test content", grade=5)
        homework.delete()

        self.student.refresh_from_db()
        self.assertEqual(self.student.avg_grade, 0.0)


class GradeValidatorTest(TestCase):

    def setUp(self):
        self.validator = GradeValidator()

    def test_valid_grade_within_range(self):
        try:
            self.validator(3)
        except ValidationError:
            self.fail("ValidationError")

    def test_invalid_grade_too_low(self):
        with self.assertRaises(ValidationError) as context:
            self.validator(1)

        self.assertIn(
            'The grade must be between 2 and 6.',
            str(context.exception),
            f"Expected error message about grade range, got: {str(context.exception)}"
        )

    def test_invalid_grade_too_high(self):
        with self.assertRaises(ValidationError) as context:
            self.validator(7)

        self.assertIn(
            'The grade must be between 2 and 6.',
            str(context.exception),
            f"Expected error message about grade range, got: {str(context.exception)}"
        )