from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, date_birth, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                date_birth=date_birth,
                **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, date_birth, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    date_birth=date_birth, **extra_fields)

    def create_superuser(self, email, first_name, last_name, date_birth, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, first_name, last_name, date_birth, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)
    date_birth = models.DateTimeField(_('date of birth'))

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_admin = models.BooleanField(_('admin'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_birth']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        """
        # Simplest possible answer: All admins are staff
        return self.is_admin


class ViewerManager(models.Manager):

    def create_viewer(self, user: User):
        viewer = self.model(user=user)
        viewer.save(using=self._db)
        return viewer


class ViewerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ViewerManager()

class ContentCreatorManager(models.Manager):

    def create_cc(self, user: User):
        cc = self.model(user=user)
        cc.save(using=self._db)
        return cc

class ContentCreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ContentCreatorManager()
