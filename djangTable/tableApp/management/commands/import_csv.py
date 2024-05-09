from django.core.management.base import BaseCommand
from tableApp.models import Person
import csv
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Loads data from CSV into the database'

    def random_date(self, start, end):
        """Generate a random datetime between `start` and `end`."""
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

    def handle(self, *args, **options):
        # Define the date range for the random date_added
        start_date = datetime(2020, 1, 1)
        end_date = datetime.now()

        with open('tableApp/Sleep_health_and_lifestyle_dataset.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bp_values = row['Blood Pressure'].split('/')
                systolic_bp = int(bp_values[0]) if len(bp_values) > 1 else 0  # Default to 0 if parsing fails
                diastolic_bp = int(bp_values[1]) if len(bp_values) > 1 else 0

                Person.objects.create(
                    person_id=int(row['Person ID']),
                    gender=row['Gender'],
                    age=int(row['Age']),
                    occupation=row['Occupation'],
                    sleep_duration=float(row['Sleep Duration']),
                    quality_sleep=int(row['Quality of Sleep']),
                    physical_activity_level=int(row['Physical Activity Level']),
                    stress_level=int(row['Stress Level']),
                    bmi_category=row['BMI Category'],
                    systolic_bp=systolic_bp,
                    diastolic_bp=diastolic_bp,
                    heart_rate=int(row['Heart Rate']),
                    daily_steps=int(row['Daily Steps']),
                    sleep_disorder=row['Sleep Disorder'],
                    date_added=self.random_date(start_date, end_date)  # Set a random date
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data into database'))
