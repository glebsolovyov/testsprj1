from django.db import models


class Tests(models.Model):
    test_name = models.CharField(max_length=255)
    questions = models.JSONField()
    questions_count = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)


class TrueAnswers(models.Model):
    true_answer = models.JSONField()
    test_id = models.IntegerField()
