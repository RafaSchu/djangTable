from django.db import models
import datetime

class Person(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # Define other fields based on your columns
    person_id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    sleep_duration = models.FloatField()
    quality_sleep = models.IntegerField()
    physical_activity_level = models.IntegerField()
    stress_level = models.IntegerField()
    bmi_category = models.CharField(max_length=50)
    systolic_bp = models.IntegerField()
    diastolic_bp = models.IntegerField()
    heart_rate = models.IntegerField()
    daily_steps = models.IntegerField()
    sleep_disorder = models.CharField(max_length=50)

    # Automatically sets the field to now when the object is first created
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.person_id)
