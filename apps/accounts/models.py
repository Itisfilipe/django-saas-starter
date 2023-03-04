import datetime

import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

from apps.accounts.constants import TIMEZONES_CHOICES, LANGUAGES_CHOICES
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(
        _("username"),
        max_length=150,
        db_index=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        blank=True,
        null=True
    )
    email = models.EmailField(_("email address"), unique=True)
    email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["username"], condition=Q(username__isnull=False), name="unique_username"),
        ]

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        self.email = self.__class__.objects.normalize_email(self.email)
        self.username = self.__class__.objects.normalize_username(self.username)


class Account(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="accounts")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=100, default="UTC", choices=TIMEZONES_CHOICES)
    language = models.CharField(max_length=10, default="en", choices=LANGUAGES_CHOICES)

    def now(self):
        """
        Returns a timezone aware datetime localized to the accounts's timezone.
        """
        now = datetime.datetime.utcnow().replace(tzinfo=pytz.timezone("UTC"))
        return now.astimezone(pytz.timezone(self.timezone))

    def localtime(self, value):
        """
        Given a datetime object as value convert it to the timezone of
        the accounts.
        """
        if value.tzinfo is None:
            value = pytz.timezone(settings.TIME_ZONE).localize(value)
        return value.astimezone(pytz.timezone(self.timezone))
