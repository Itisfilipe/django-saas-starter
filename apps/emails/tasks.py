import logging
from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from apps.emails.models import Email

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def cleanup_old_sent_emails():
    emails_to_delete = Email.objects.filter(status=Email.Status.SENT, sent_at__lt=timezone.now() - timedelta(days=30))
    for email in emails_to_delete:
        logger_message = f"Deleting email {email.id}, sent to {email.to}, " \
                   f"with subject {email.subject} and status {email.status}\n " \
                   f"html: {email.html}\n " \
                   f"plain_text: {email.plain_text}"
        logger.info(logger_message)
        email.delete()
