import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By inheriting from `BaseUserManager`,
    we get a lot of the same code used by Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, first_name, last_name, password):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have an username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if first_name is None:
            raise TypeError('Users must have a first name.')

        if last_name is None:
            raise TypeError('Users must have a last name.')

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        user = self.create_user(username, email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # We will use the email for logging in because it is one of the most common form of login credential.
    # We will also use the email for contacting the user
    # We want to index this column in the database to improve lookup performance.
    email = models.EmailField(
        _('email address'),
        db_index=True,
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )

    # Each `User` needs a human-readable unique identifier that we can use to represent the `User` in the UI.
    # We want to index this column in the database to improve lookup performance.
    username = models.CharField(
        _('username'),
        max_length=150,
        db_index=True,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )

    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last connection'), default=timezone.now)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        )
    )
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )

    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.first_name

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=1)
        print('--------- ', dt.strftime('%s'))
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def save(self, *args, **kwargs):
        self.last_login = timezone.now()
        super(User, self).save(*args, **kwargs)
