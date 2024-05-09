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
                Person.objects.create(
                    person_id=int(row['person_id']),
                    gender=row['gender'],
                    age=int(row['age']),
                    occupation=row['occupation'],
                    sleep_duration=float(row['sleep_duration']),
                    quality_sleep=row['quality_sleep'].lower() in ['true', '1', 't', 'yes'],
                    physical_activity_level=row['physical_activity_level'],
                    stress_level=int(row['stress_level']),
                    bmi_category=row['bmi_category'],
                    blood_pressure=row['blood_pressure'],
                    heart_rate=int(row['heart_rate']),
                    daily_steps=int(row['daily_steps']),
                    sleep_disorder=row['sleep_disorder'].lower() in ['true', '1', 't', 'yes'],
                    date_added=self.random_date(start_date, end_date)  # Set a random date
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data into database'))
