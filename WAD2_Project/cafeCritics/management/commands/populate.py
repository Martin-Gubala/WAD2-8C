import os
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cafeCritics.models import UserProfile, Cafe, Drink, Review

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WAD2_Project.settings")

import django
django.setup()

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.populate_users()
        self.populate_cafes()
        self.populate_drinks()  # Add drinks after cafes
        self.populate_reviews()

    def populate_users(self):
        # Create 5 business users
        business_users = [
            {'username': 'business1', 'email': 'business1@example.com'},