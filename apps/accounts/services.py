import logging
import smtplib

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string

from apps.accounts.models import Account, CustomUser
from apps.emails.services import send_single_mail

logger = logging.getLogger(__name__)


def send_create_account_confirmation_email(email, full_name):
    subject = render_to_string("accounts/email/confirmation_email/subject.txt", {"full_name": full_name})
    message_text = render_to_string("accounts/email/confirmation_email/body.txt", {"full_name": full_name, "email": email})
    message_html = render_to_string("accounts/email/confirmation_email/body.html", {"full_name": full_name, "email": email})
    from_email = settings.DEFAULT_FROM_EMAIL
    try:
        send_single_mail(
            subject=subject,
            message_text=message_text,
            message_html=message_html,
            from_email=from_email,
            to_email=[email]
        )
    except smtplib.SMTPException:
        logger.warning("Failed to send email to %s", email, exc_info=True)


def _create_user(email, password, username=None):
    user = CustomUser(
        username=username,
        email=email,
    )
    user.password = make_password(password)
    user.full_clean()
    user.save()
    return user


def create_account(*, email, password, full_name, language, timezone):
    user = _create_user(
        email=email,
        password=password,
        username=email,
    )
    account = Account(
        user=user,
        full_name=full_name,
        language=language,
        timezone=timezone,
    )
    account.full_clean()
    account.save()
    send_create_account_confirmation_email(email, full_name)
    return account
