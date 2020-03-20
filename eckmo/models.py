from django.contrib.postgres.fields import JSONField

class Answer(models.Model):
    answer = JSONField()
