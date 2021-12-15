from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    special = models.IntegerField()
    right_answer = models.IntegerField(default=0)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id = models.IntegerField()
    answer_text = models.CharField(max_length=200)
    points = models.IntegerField(default=0)


