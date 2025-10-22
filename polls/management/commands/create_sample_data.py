from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice


class Command(BaseCommand):
    help = "Creates sample poll questions for demonstration"

    def handle(self, *args, **options):
        # Check if questions already exist
        if Question.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Sample data already exists. Skipping.")
            )
            return

        # Create sample questions
        q1 = Question.objects.create(
            question_text="What's your favorite programming language?",
            pub_date=timezone.now(),
        )
        Choice.objects.create(choice_text="Python", question=q1, votes=0)
        Choice.objects.create(choice_text="JavaScript", question=q1, votes=0)
        Choice.objects.create(choice_text="Java", question=q1, votes=0)
        Choice.objects.create(choice_text="C++", question=q1, votes=0)

        q2 = Question.objects.create(
            question_text="What's your preferred development environment?",
            pub_date=timezone.now(),
        )
        Choice.objects.create(choice_text="VS Code", question=q2, votes=0)
        Choice.objects.create(choice_text="PyCharm", question=q2, votes=0)
        Choice.objects.create(choice_text="Vim", question=q2, votes=0)
        Choice.objects.create(choice_text="Emacs", question=q2, votes=0)

        q3 = Question.objects.create(
            question_text="How do you prefer to learn new technologies?",
            pub_date=timezone.now(),
        )
        Choice.objects.create(choice_text="Online courses", question=q3, votes=0)
        Choice.objects.create(choice_text="Documentation", question=q3, votes=0)
        Choice.objects.create(choice_text="Video tutorials", question=q3, votes=0)
        Choice.objects.create(choice_text="Hands-on projects", question=q3, votes=0)

        self.stdout.write(
            self.style.SUCCESS("Successfully created sample poll questions!")
        )
