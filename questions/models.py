from django.db import models


class Questions(models.Model):
    question = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='questions')
    answer = models.CharField(max_length=50)
    is_correct = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer
