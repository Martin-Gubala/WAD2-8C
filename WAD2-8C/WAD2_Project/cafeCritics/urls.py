from django.urls import path
from . import views
from .views import home_view, signup_view, login_view, cafe_setup_view

app_name = 'cafeCritics'

urlpatterns = [
    # Home page route
    path('', views.home_view, name='home_page'), #Displays the main homepage of the application

    # Display all cafe with filters applied through GET request
    path('cafes/', views.cafes_view, name='cafes'), # List all cafes or filter by ratings

    # Search function for cafes
    path('search/', views.search_results, name='search'), # Handles search queries within the site

    # Static about page
    path('about/', views.about_view, name='about'), # Provides information about the Cafe Critics platform

    # User account settings page
    path('accountsettings/', views.account_settings_view, name='account_settings'), # Allows users to adjust their account settings

    # Detail view for a specific cafe by slug
    path('cafes/<slug:cafe_name_slug>/', views.show_cafe, name='show_cafe'), # Displays detaled info about a specific cafe

    # Displays drinks offered by a specific cafe
    path('cafes/<slug:cafe_name_slug>/drinks', views.show_drinks, name='show_drinks'), # Shows drinks available at a specific cafe 

    # AJAX route for updating cafe details dynamically
    path('cafes/<slug:cafe_name_slug>/AJAX', views.show_cafeAJAX, name='show_cafeAJAX'), # For dynamic content updates without reloading the page

    # Allows users to submit reviews for a specific cafe
    path('cafes/<slug:cafe_name_slug>/review/', views.review_view, name='review'), # Handles posting of reviews to cafes

    # Routes for user registration and login
    path('signup/', views.signup_view, name='signup'), # User registration page
    path('login/', views.login_view, name='login'), # User login page

    # Cafe setup page for registration users 
    path('cafe_setup/', views.cafe_setup_view, name='cafe_setup'), # Allows users to add new cafes to the platform 

    # Logout route
    path('logout/', views.logout_view, name='logout'),# Logs out the current user and redirects to home page

    # User profile page, diplays user details and activities
    path('profile/<str:username>/', views.profile_view, name='profile'),  # Shows the profile of a user, including their cafes and reviews if applicable

    # Edit details of a specific cafe
    path('cafe/<slug:cafe_name_slug>/edit/', views.edit_cafe_view, name='edit_cafe'), # Allows cafe owners to edit their cafe details
]
