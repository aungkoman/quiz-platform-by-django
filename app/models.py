from django.db import models

# Create your models here.

class Quiz(models.Model):  
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()

    # methods
    def __str__(self):
        return self.title