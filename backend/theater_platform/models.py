from django.db import models

from user_management.models import ViewerProfile as Viewer
from user_management.models import ContentCreatorProfile as ContentCreator


class Category(models.Model):
    name = models.CharField(max_length=128)


class AlbumContent(models.Model):
    creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    date_creation = models.DateField()
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=6, decimal_places=2)


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
    date_register = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=2)
    is_paid = models.BooleanField()


class ContentPurchase(Purchase):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)


class AlbumPurchase(Purchase):
    album = models.ForeignKey(AlbumContent, on_delete=models.CASCADE)


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
