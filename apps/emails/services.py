from core.exceptions import ApplicationError


def send_single_mail(*, subject, from_email, to_email, message_text=None, message_html=None, sync=False):
    if not message_text and message_html:
        raise ApplicationError
