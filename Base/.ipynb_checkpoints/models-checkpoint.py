from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    #temp_gender=models.CharField(max_length=10)
    gender = models.IntegerField()
    education = models.CharField(max_length=100)
    income=models.IntegerField()
    fees=models.IntegerField()
    

    def __str__(self):
        return self.name