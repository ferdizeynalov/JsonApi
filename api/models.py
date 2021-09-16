from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    score = models.IntegerField(default=0)
    
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    first_name = models.CharField(_('First name'), max_length=150, blank=True)
    last_name = models.CharField(_('Last name'), max_length=150, blank=True)
    USERNAME_FIELD = "username"


    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    