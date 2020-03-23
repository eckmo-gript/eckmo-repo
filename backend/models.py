from django.db import models
from django.utils import timezone


class Answer(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    delivered_at = models.DateTimeField(auto_now_add=True)
    confidence_score = models.IntegerField()


class Entry(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    arrived_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.TextField()

    def timestamp(self):
        self.arrived_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
