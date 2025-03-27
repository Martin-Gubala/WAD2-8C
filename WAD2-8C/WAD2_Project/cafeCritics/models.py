from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


# Represents a user profile, extending the default User model with additional attributes
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Links UserProfile to a user instance
    user_type = models.CharField(max_length=20, choices=(('personal', 'Personal'), ('business', 'Business')))

    def __str__(self):
        return self.user.username # Returns the username for display purposes

# Represents a cafe with a name, location, and associated owner from the User model.
class Cafe(models.Model):
    name = models.CharField(max_length=20) # Name of the cafe
    location = models.CharField(max_length=20) # Physical location of the cafe
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cafe") # Ensure one cafe per user
    average_rating = models.FloatField(default=0.0) # Average rating as a float with a default value
    slug = models.SlugField(unique=True) # URL-friendly slug derived from the cafe name
    photo = models.ImageField(upload_to='cafe_photos/', blank=True, null=True)  # Save images in 'media/cafe_photos/'

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't exist
            self.slug = slugify(self.name)
            # Ensure the slug is unique
            unique_slug = self.slug
            num = 1
            while Cafe.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{num}"
                num += 1
            self.slug = unique_slug
        super(Cafe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name # Displays the cafe name when the model instance is called

# Represents a drink available at a cafe, with fields for name, price, and associated cafe
class Drink(models.Model):
    name = models.CharField(max_length=20) # Name of the drink
    price = models.DecimalField(max_digits=6, decimal_places=2) # Price of the drink as a decimal
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='drinks') # References the cafe offering the drink
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)  # Average rating for the drink
 

    def __str__(self):
        return self.name # Returns the name of the drink for display purposes
    
# Represents a review for a cafe, linked to a user and a cafe
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews") # User who authored the review 
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="cafe_reviews") # Cafe being reviewed 
    text = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # Rating provided by the user
    

    class Meta:
        unique_together = ('user', 'cafe') # Ensures a user can only review a cafe once

    def __str__(self):
        return f"Review by {self.user.username} for {self.cafe.name}" # Formats the string representation of the review