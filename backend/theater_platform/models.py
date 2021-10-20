from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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


class Viewer(User):
    pass


class ContentCreator(User):
    pass


class AlbumContent(models.Model):
    creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date_creation = models.DateField()


class Content(models.Model):
    album = models.ForeignKey(AlbumContent, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    filepath = models.FilePathField()


class Photo(Content):
    pass


class Video(Content):
    duration = models.IntegerField()


class Purchase(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    album = models.ForeignKey(AlbumContent, on_delete=models.CASCADE)
    date_register = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=2)
    is_paid = models.BooleanField()


class Subscription(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    album = models.ForeignKey(AlbumContent, on_delete=models.CASCADE)
    date_register = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=2)


class Payment(models.Model):
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date_creation = models.DateField()
    is_paid = models.BooleanField()


class PaymentPurchase(Payment):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)


class PaymentSubscription(Payment):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)


class MoneyTransference(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    bank_account = models.CharField(max_length=11)