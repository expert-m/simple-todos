from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from project.apps.organizations.models import Organization
from project.apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    organizations = models.ManyToManyField(Organization, related_name='users')
    active_organization = models.ForeignKey(Organization, related_name='+',
                                            null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
