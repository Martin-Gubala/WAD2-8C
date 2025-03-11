from django.urls import path
from .import views 
from .views import home_view

app_name = 'cafeCritics'

urlpatterns = [
    path('register/', views.register, name='register' ),
    path('', home_view, name='home_page'),
    path('cafes/', views.cafes_view, name='cafes'),
    path('about/', views.about_view, name='about'),
    path('accountsettings/', views.account_settings_view, name='account_settings'),
    path('cafes/<int:cafe_id>/', views.cafe_view, name='cafe'),
    path('cafes/<int:cafe_id>/review', views.review_view, name='review'),
]
