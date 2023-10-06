from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "@johndoe",
            first_name = "John",
            last_name = "Doe",
            email="johndoe@example.org",
            password="Password123",
            bio="This is a bio."
        )


    def test_valid_user(self):
        self._assert_user_is_valid()

    def test_invalid_user(self):
        self.user.username = ""
        self._assert_user_is_invalid()
    
    def test_username_can_be_30_chars_long(self):
        self.user.username = "@" + "x" * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_31_chars_long(self):
        self.user.username = "@" + "x" * 30
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        User.objects.create_user(
            "@janedoe",
            first_name = "Jane",
            last_name = "Doe",
            email="janedoe@example.org",
            password="Password123",
            bio="This is a bio for Jane."
        )
        self.user.username = "@janedoe"
        self._assert_user_is_invalid()

    def test_username_starts_with_at(self):
        self.user.username="johndoe"
        self._assert_user_is_invalid

    def test_username_only_has_alphanumericals_after_at(self):
        self.user.username="@john!doe"
        self._assert_user_is_invalid

    def test_username_must_contain_at_least_3_alphanumericals(self):
        self.user.username="@jo"
        self._assert_user_is_invalid

    def test_username_may_contain_numbers(self):
        self.user.username="@j0hndoe"
        self._assert_user_is_valid

    def test_username_must_contain_only_one_at(self):
        self.user.username="@@johndoe"
        self._assert_user_is_invalid



    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail("Test user should be valid")
    
    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
    
