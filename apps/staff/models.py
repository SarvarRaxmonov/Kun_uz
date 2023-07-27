from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Team(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team_images/")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    theme = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.name
