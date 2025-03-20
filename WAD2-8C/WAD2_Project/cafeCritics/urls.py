from django.urls import path
from . import views
from .views import home_view, no_access_view, signup_view, login_view, cafe_setup_view

app_name = 'cafeCritics'

urlpatterns = [
    path('', home_view, name='home_page'),
    path('cafes/', views.cafes_view, name='cafes'),
    path('search/', views.search_results, name='search'),
    path('about/', views.about_view, name='about'),
    path('accountsettings/', views.account_settings_view, name='account_settings'),
    path('cafes/<slug:cafe_name_slug>/', views.show_cafe, name='show_cafe'),  # Corrected URL pattern
    path('cafes/<slug:cafe_name_slug>/drinks', views.show_drinks, name='show_drinks'),
    path('cafes/<slug:cafe_name_slug>/AJAX', views.show_cafeAJAX, name='show_cafeAJAX'),
    path('cafes/<slug:cafe_name_slug>/review/', views.review_view, name='review'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('cafe_setup/', cafe_setup_view, name='cafe_setup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),  # Added URL pattern for profile view
    path('cafe/<slug:cafe_name_slug>/edit/', views.edit_cafe_view, name='edit_cafe'),
    path('no_access/', no_access_view, name='no_access'),
]
