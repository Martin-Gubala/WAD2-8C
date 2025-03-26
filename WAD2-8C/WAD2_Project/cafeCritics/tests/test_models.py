from django.test import TestCase
from django.contrib.auth.models import User
from cafeCritics.models import UserProfile, Cafe, Drink, Review

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = UserProfile.objects.create(user=self.user, user_type="personal")
    
    def test_str(self):
        self.assertEqual(str(self.profile), "testuser")

class CafeModelTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="cafeowner", password="testpass")
        self.cafe = Cafe.objects.create(name="Test Cafe", location="Test Location", owner=self.owner)
    
    def test_slug_generation(self):
        # Ensure that a slug is generated and is slugified correctly
        self.assertTrue(self.cafe.slug)
        self.assertEqual(self.cafe.slug, "test-cafe")
    
    def test_slug_uniqueness(self):
        # Creating a second cafe with the same name should generate a unique slug.
        owner2 = User.objects.create_user(username="cafeowner2", password="testpass")
        cafe2 = Cafe.objects.create(name="Test Cafe", location="Another Location", owner=owner2)
        self.assertNotEqual(self.cafe.slug, cafe2.slug)
    
    def test_str(self):
        self.assertEqual(str(self.cafe), "Test Cafe")

class DrinkModelTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="cafeowner", password="testpass")
        self.cafe = Cafe.objects.create(name="Test Cafe", location="Test Location", owner=self.owner)
        self.drink = Drink.objects.create(name="Espresso", price=2.50, cafe=self.cafe, rating=4)
    
    def test_str(self):
        self.assertEqual(str(self.drink), "Espresso")
    
    def test_drink_rating_choices(self):
        # Ensure the rating is within the allowed range (1 to 5)
        self.assertIn(self.drink.rating, range(1, 6))

class ReviewModelTest(TestCase):
    def setUp(self):
        self.reviewer = User.objects.create_user(username="reviewer", password="testpass")
        self.owner = User.objects.create_user(username="cafeowner", password="testpass")
        self.cafe = Cafe.objects.create(name="Review Cafe", location="Test Location", owner=self.owner)
        self.review = Review.objects.create(user=self.reviewer, cafe=self.cafe, text="Great cafe!", rating=5)
    
    def test_str(self):
        expected = f"Review by {self.reviewer.username} for {self.cafe.name}"
        self.assertEqual(str(self.review), expected)
    
    def test_unique_together(self):
        # Trying to create a second review for the same cafe by the same user should raise an error.
        with self.assertRaises(Exception):
            Review.objects.create(user=self.reviewer, cafe=self.cafe, text="Another review", rating=4)