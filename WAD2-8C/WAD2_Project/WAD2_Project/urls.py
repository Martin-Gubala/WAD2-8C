"""WAD2_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cafeCritics.views import home_view  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL pattern for admin site
    path('admin/', admin.site.urls),

    # URL pattern for user login, utilitizing Django's built in login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # URL pattern to include all URLs from the cafeCritics application
    path('', include('cafeCritics.urls', namespace='cafeCritics')),  

    # Direct URL to the home page of the site
    path('home/', home_view, name='home_page'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
