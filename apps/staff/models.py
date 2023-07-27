from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

