import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cafeCritics.models import UserProfile, Cafe, Drink, Review

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.populate_users()
        self.populate_cafes()
        self.populate_reviews()

    def populate_users(self):
        # Create 6 business users
        business_users = [
            {'username': 'business1', 'email': 'business1@example.com'},
            {'username': 'business2', 'email': 'business2@example.com'},
            {'username': 'business3', 'email': 'business3@example.com'},
            {'username': 'business4', 'email': 'business4@example.com'},
            {'username': 'business5', 'email': 'business5@example.com'},
            {'username': 'business6', 'email': 'business6@example.com'},
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
        # Get business users: assign 1 cafe to each business user => 6 cafes total.
        business_profiles = list(UserProfile.objects.filter(user_type='business'))
        cafes_data = [
            {'name': 'Cafe Sunrise', 'location': 'Downtown', 'average_rating': 4},
            {'name': 'Moonlight Coffee', 'location': 'Uptown', 'average_rating': 5},
            {'name': 'Starbucks Corner', 'location': 'Midtown', 'average_rating': 4},
            {'name': 'Brewed Awakening', 'location': 'East Side', 'average_rating': 5},
            {'name': 'The Daily Grind', 'location': 'West End', 'average_rating': 3},
            {'name': 'Bean There', 'location': 'Central District', 'average_rating': 4},
        ]
        # Assign one cafe per business user
        for idx, cafe_data in enumerate(cafes_data):
            owner_profile = business_profiles[idx]
            cafe = Cafe.objects.create(
                name=cafe_data['name'],
                location=cafe_data['location'],
                owner=owner_profile.user,
                average_rating=cafe_data['average_rating']
            )
            # Create 3 drinks for each cafe
            drinks = [
                {
                    'name': 'Espresso',
                    'price': 2.00,
                    'rating': random.randint(3, 5),
                },
                {
                    'name': 'Latte',
                    'price': 3.50,
                    'rating': random.randint(3, 5),
                },
                {
                    'name': 'Cappuccino',
                    'price': 3.00,
                    'rating': random.randint(3, 5),
                },
            ]
            for drink_data in drinks:
                Drink.objects.create(
                    name=drink_data['name'],
                    price=drink_data['price'],
                    cafe=cafe,
                    rating=drink_data['rating']
                )

    def populate_reviews(self):
        import itertools
        # Get all personal users and all cafes
        personal_profiles = list(UserProfile.objects.filter(user_type='personal'))
        cafes = list(Cafe.objects.all())
        for profile in personal_profiles:
            # Select 4 unique cafes for this user (avoiding duplicates because of unique_together)
            if len(cafes) >= 4:
                selected_cafes = random.sample(cafes, 4)
            else:
                selected_cafes = cafes
            for idx, cafe in enumerate(selected_cafes, start=1):
                Review.objects.create(
                    user=profile.user,
                    cafe=cafe,
                    text=f"Review {idx} from {profile.user.username} for {cafe.name}. A delightful experience!",
                    rating=random.randint(3, 5)
                )
