from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=(('personal', 'Personal'), ('business', 'Business')))

    def __str__(self):
        return self.user.username

class Cafe(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cafes")
    average_rating = models.IntegerField()
    #url = models.URLField(); need to add to database

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='drinks')
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # Ratings 1-5

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="cafe_reviews")
    text = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # Ratings 1-5

    class Meta:
        unique_together = ('user', 'cafe')

    def __str__(self):
        return f"Review by {self.user.username} for {self.cafe.name}"