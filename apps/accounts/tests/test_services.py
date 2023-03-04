from unittest.mock import patch, MagicMock

from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.test import TestCase

from apps.accounts.models import Account
from apps.accounts.services import create_account

User = get_user_model()


class CreateAccountTestCase(TestCase):

    def setUpTestData(cls):
        cls.account_payload = {
            "email": "test@test.com",
            "password": User.objects.make_random_password(),
            "full_name": "Fake Full Name",
            "language": "en",
            "timezone": "UTC",
        }

    def test_should_create_an_account_with_a_user(self):
        create_account(**self.account_payload)
        assert User.objects.filter(email=self.account_payload["email"]).exists()
        assert Account.objects.filter(user__email=self.account_payload["email"]).exists()

    def test_should_return_account(self):
        account = create_account(**self.account_payload)
        assert isinstance(account, Account)

    def test_should_send_confirmation_email(self, send_email_mock: MagicMock):
        subject = render_to_string("accounts/email/confirmation_email/subject.txt", {"full_name": self.account_payload["full_name"]})
        message_text = render_to_string("accounts/email/confirmation_email/body.txt", {"full_name": self.account_payload["full_name"], "email": self.account_payload["email"]})
        message_html = render_to_string("accounts/email/confirmation_email/body.html", {"full_name": self.account_payload["full_name"], "email": self.account_payload["email"]})
        from_email = settings.DEFAULT_FROM_EMAIL
        create_account(**self.account_payload)
        send_email_mock.assert_called_once_with(
            subject=subject,
            from_email=from_email,
            to_email=self.account_payload["email"],
            message_text=message_text,
            message_html=message_html
        )
