from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Session(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(blank=True, default=0)
    subtopic = models.ForeignKey(SubTopic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return self.started_at.strftime("%m/%d/%Y, %H:%M:%S")
