from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.text[:100]}...' if len(self.text) > 100 else self.text


class Answer(models.Model):
    SCORE_TYPES = (
        (1, 'max_agree'),
        (2, 'med_agree'),
        (3, 'min_agree'),
        (4, 'neutral'),
        (5, 'min_disagree'),
        (6, 'med_disagree'),
        (7, 'max_disagree'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORE_TYPES, blank=None)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.score}'
