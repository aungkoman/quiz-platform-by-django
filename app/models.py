from django.db import models

from django.contrib.auth.models import User # Built-in user model
# Create your models here.

class Quiz(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()

    # methods
    def __str__(self):
        return self.title

class Question(models.Model):  
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.TextField()

    # methods
    def __str__(self):
        return self.title