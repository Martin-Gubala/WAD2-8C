from django.urls import path
from .import views 
from .views import home_view

app_name = 'cafeCritics'

urlpatterns = [
    path('register/', views.register, name='register' ),
    path('', home_view, name='home_page')
]
