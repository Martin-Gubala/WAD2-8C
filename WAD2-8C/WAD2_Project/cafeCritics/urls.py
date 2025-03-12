from django.urls import path
from .import views 
from .views import home_view, signup_view, login_view, cafe_setup_view

app_name = 'cafeCritics'

urlpatterns = [
    path('', home_view, name='home_page'),
    path('cafes/', views.cafes_view, name='cafes'),
    path('search/', views.search_results, name='search'),
    path('about/', views.about_view, name='about'),
    path('accountsettings/', views.account_settings_view, name='account_settings'),
    path('cafes/<int:cafe_id>/', views.cafe_view, name='cafe'),
    path('cafes/<int:cafe_id>/review', views.review_view, name='review'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('cafe_setup/', cafe_setup_view, name='cafe_setup'),
]
