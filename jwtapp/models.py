from django.db import models

class userdetails(models.Model):
    phone=models.BigIntegerField(max_length=10)
    username=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    state=models.CharField(max_length=20)
    obeject=models.Manager()

    def __str__(self):
        return self.username
