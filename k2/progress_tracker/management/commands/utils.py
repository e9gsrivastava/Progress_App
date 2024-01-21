import random
from django.core.management.base import BaseCommand
from progress_tracker.models import Trainee, ProgressReport
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "generate random data for trainees and progress reports"

    def handle(self, *args, **options):
        self.generate_random_data()

    def generate_random_data(self):
        User.objects.create_user(username="mentor", password="mentor_password")
        trainee_names = ["Akbar", "Shivansh", "kunal", "Akash", "Gaurav"]
        trainees = []

        for name in trainee_names:
            trainee = Trainee.objects.create(username=f"e9{name.lower()}", name=name)
            trainees.append(trainee)

        for trainee in trainees:
            for week_number in range(1, 11):
                attendance = random.randint(80, 100)
                assignment = random.randint(60, 100)
                marks = random.randint(50, 100)
                comments = f"Week {week_number}  good."

                ProgressReport.objects.create(
                    trainee=trainee,
                    week_number=week_number,
                    attendance=attendance,
                    assignment=assignment,
                    marks=marks,
                    comments=comments,
                )

        self.stdout.write(self.style.SUCCESS("successful."))
