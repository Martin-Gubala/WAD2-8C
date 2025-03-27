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
        self.populate_reviews()

    def populate_users(self):
        # Create 5 business users
        business_users = [
            {'username': 'business1', 'email': 'business1@example.com'},
            {'username': 'business2', 'email': 'business2@example.com'},
            {'username': 'business3', 'email': 'business3@example.com'},
            {'username': 'business4', 'email': 'business4@example.com'},
            {'username': 'business5', 'email': 'business5@example.com'}
        ]
        for user_data in business_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password='simplepassword'
                )
                UserProfile.objects.create(user=user, user_type='business')

        # Create 5 personal users
        personal_users = [
            {'username': 'personal1', 'email': 'personal1@example.com'},
            {'username': 'personal2', 'email': 'personal2@example.com'},
            {'username': 'personal3', 'email': 'personal3@example.com'},
            {'username': 'personal4', 'email': 'personal4@example.com'},
            {'username': 'personal5', 'email': 'personal5@example.com'},
        ]
        for user_data in personal_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password='simplepassword'
                )
                UserProfile.objects.create(user=user, user_type='personal')

    def populate_cafes(self):
        # Get business users: assign 1 cafe to each business user
        business_profiles = list(UserProfile.objects.filter(user_type='business'))
        cafes_data = [
            {'name': 'Moonlight Coffee', 'location': 'Uptown', 'average_rating': 5, 'photo': 'cafe_photos/moonlight.jpg'},
            {'name': 'Starbucks Corner', 'location': 'Midtown', 'average_rating': 4, 'photo': 'cafe_photos/starbucks.jpg'},
            {'name': 'Brewed Awakening', 'location': 'East Side', 'average_rating': 5, 'photo': 'cafe_photos/brewed.jpg'},
            {'name': 'The Daily Grind', 'location': 'West End', 'average_rating': 3, 'photo': 'cafe_photos/dailygrind.jpg'},
            {'name': 'Bean There', 'location': 'Central District', 'average_rating': 4, 'photo': 'cafe_photos/beanthere.jpg'},
        ]
        for idx, cafe_data in enumerate(cafes_data):
            owner_profile = business_profiles[idx]
            cafe = Cafe.objects.create(
                name=cafe_data['name'],
                location=cafe_data['location'],
                owner=owner_profile.user,
                average_rating=cafe_data['average_rating'],
                photo=cafe_data['photo']  # Assign photo
            )
            # Create 3 drinks for each cafe
            drinks = [
                {'name': 'Espresso', 'price': 2.00, 'rating': random.randint(3, 5)},
                {'name': 'Latte', 'price': 3.50, 'rating': random.randint(3, 5)},
                {'name': 'Cappuccino', 'price': 3.00, 'rating': random.randint(3, 5)},
            ]
            for drink_data in drinks:
                Drink.objects.create(
                    name=drink_data['name'],
                    price=drink_data['price'],
                    cafe=cafe,
                    rating=drink_data['rating'],
                    ratings_total=drink_data['rating'] * 10,
                    ratings_no=10
                )

    def populate_reviews(self):
        # Get all personal users and all cafes
        personal_profiles = list(UserProfile.objects.filter(user_type='personal'))
        cafes = list(Cafe.objects.all())
        review_texts = [
            "A delightful experience!",
            "The coffee was amazing, and the ambiance was perfect.",
            "Great place to relax and enjoy a cup of coffee.",
            "The staff was friendly, and the drinks were top-notch.",
            "Highly recommend this cafe for coffee lovers!",
        ]
        for cafe in cafes:
            for profile in random.sample(personal_profiles, min(3, len(personal_profiles))):  # Assign 3 reviews per cafe
                Review.objects.create(
                    user=profile.user,
                    cafe=cafe,
                    text=random.choice(review_texts),
                    rating=random.randint(3, 5)
                )
