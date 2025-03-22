from django.contrib import admin
from .models import UserProfile, Cafe, Drink, Review 

# Register models for the Django admin panel to allow for easy management of data entries related to cafes.
# Register UserProfile for administration in the Django admin interface.
# This enables admins to view and manage user profiles directly from the admin panel.
admin.site.register(UserProfile)
"""
Register the Cafe to enable administrative actions on cafe entries. This allows for the addition, editing, or deletion of cafes through the admin interface.
"""
admin.site.register(Cafe)

"""
Register drinks to manage beverage items related to cafes. Admins can supervise details such as names, prices, and ratings.
"""
admin.site.register(Drink)

"""
Register for Review to manage user-submitted reviews of cafes. 
This registration will help moderate the reviews for appropriateness and accuracy.
"""
admin.site.register(Review)

# Custom admin class for Cafe that prepopulates the slug field from the cafe name
class CafeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name')}

"""
Verify if the Cafe is already registered to prevent duplicates, and then register it with customized admin settings. 
This step ensures that the Cafe URLs are user-friendly and generated automatically from their names.
"""
if not admin.site.is_registered(Cafe):
    admin.site.register(Cafe, CafeAdmin)
