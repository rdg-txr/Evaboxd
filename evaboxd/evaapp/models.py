from django.db import models


class Show(models.Model):
    show_title = models.CharField(length=200)
    date_release = models.DateTimeField("date release")

    def __str__(self):
        return self.title


class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ep_title = models.CharField(length=200)
    