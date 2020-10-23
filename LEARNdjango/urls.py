'''
LEARNdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
'''
from django.contrib import admin
from django.contrib.auth import views as auth_views # Views that django provides for us automatically
from django.urls import path, include
from users import views as user_views
# These are required for images from non stock 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Will use the url.py of blog app that uses blog/view.py user declared methods to render pages
    path('register/', user_views.register, name = 'register'), # Added to url pattern so we don't have weird paths
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'), # Provided by django, django handles a few forms and logic for us, but not the template
    # WE HAVE TO FEED LOGIN_REDIRECT_URL = 'blog-home' in the settings.py to tell where redirect upon succesfully logging in
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'), # These will go to the views.py that django automatically has and provide us a form in 'form'
    # We don't need a function in views.py to cast the 2 links above
    path('profile/', user_views.profile, name = 'profile'),
]

if settings.DEBUG: # We need this after we alter the route through which images are saved
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)