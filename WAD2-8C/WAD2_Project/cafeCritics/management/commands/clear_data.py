from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cafeCritics.models import Cafe, Drink, Review, UserProfile

class Command(BaseCommand):
    help = 'Clear all accounts, cafes, drinks, reviews, and user profiles from the database'

    def handle(self, *args, **kwargs):
        # Delete all reviews
        Review.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all reviews.'))

        # Delete all drinks
        Drink.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all drinks.'))

        # Delete all cafes
        Cafe.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all cafes.'))

        # Delete all user profiles
        UserProfile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all user profiles.'))

        # Delete all users
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all user accounts.'))

        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
