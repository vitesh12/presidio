from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=30)
    qua = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    subject = models.CharField(max_length=30) 

    def __str__(self):
        return f'{self.firstname} {self.qua}'