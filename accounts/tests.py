from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from accounts.forms import ProfileDeleteForm
from accounts.models import Student
from accounts.validators import NameValidator
from homeworks.models import Homework

# Create your tests here.

UserModel = get_user_model()


class TestUserModel(TestCase):

    def test_valid__str__method(self):
        user = UserModel.objects.create_user(username='testname', password='passwordtest987', email='strtest@test.com')
        self.assertEqual(str(user), user.email)


class ProfileDeleteFormTestCase(TestCase):
    def test_fields_are_not_required_and_disabled(self):
        form = ProfileDeleteForm()

        for field_name, field in form.fields.items():
            self.assertFalse(field.required)
            self.assertTrue('disabled' in field.widget.attrs)


class NameValidatorTest(TestCase):

    def setUp(self):
        self.validator = NameValidator()

    def test_name_with_validator(self):
        try:
            self.validator('name')
        except ValidationError:
            self.assertFalse(True)


class StudentModelTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.student = Student.objects.create(user=self.user, avg_grade=0.0)

    def test_update_avg_grade_with_graded_homework(self):

        homework1 = Homework.objects.create(student=self.student, grade=3.75, is_graded=True)
        homework2 = Homework.objects.create(student=self.student, grade=4.20, is_graded=True)
        homework3 = Homework.objects.create(student=self.student, grade=6.00, is_graded=True)

        self.student.update_avg_grade()
        expected_avg = round((3.75 + 4.20 + 6.00) / 3, 2)
        self.assertEqual((float(self.student.avg_grade)), expected_avg)

    def test_update_avg_grade_with_no_graded_homework(self):

        self.assertEqual(self.student.avg_grade, 0.0)
        self.student.update_avg_grade()
        self.assertEqual(self.student.avg_grade, 0.0)