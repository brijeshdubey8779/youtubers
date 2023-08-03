from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    fb_link = models.CharField(max_length=50)
    linkedin_link = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)
    yt_link = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/slider/%y/")
    created_date = models.DateTimeField(auto_now_add=True)
    button_link = models.CharField(max_length=500)

    def __str__(self):
        return self.headline
