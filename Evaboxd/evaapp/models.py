from django.db import models


class Show(models.Model):
    show_title = models.CharField(max_length=200)
    show_date = models.DateTimeField("date release")

    def __str__(self):
        return self.show_title


class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ep_title = models.CharField(max_length=200)
    ep_date = models.DateTimeField("date release")
    ep_season = models.IntegerField(default=0)
    ep_num = models.IntegerField(default=0)

    def __str__(self):
        return self.ep_title
