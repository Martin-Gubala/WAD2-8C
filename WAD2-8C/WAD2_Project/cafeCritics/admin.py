from django.contrib import admin
from .models import UserProfile, Cafe, Drink, Review 
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Cafe)
admin.site.register(Drink)
admin.site.register(Review)

class CafeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name')}

if not admin.site.is_registered(Cafe):
    admin.site.register(Cafe, CafeAdmin)
