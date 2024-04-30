from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import pickle

# Create your models here.
GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)

EDUCATION  = (
    (0, 'Diploma'),
    (1, 'Graduation'),
    (2, 'Post-Graduation'),
    (3, 'Undergraduation'),
)

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=100, null=True)
    age=models.PositiveIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(35)], null=True)
    gender = models.PositiveIntegerField(choices=GENDER, null=True)
    education = models.PositiveIntegerField(choices=EDUCATION, null=True)
    income=models.IntegerField(null=True)
    fees=models.IntegerField(null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        with open('recommender_system.pkl', 'rb') as file:
            model = pickle.load(file)
        self.predictions = model.predict(
            [[self.age, self.gender, self.education, self.income, self.fees]])
        return super().save(*args, *kwargs)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name