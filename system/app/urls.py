from django.contrib import admin
from django.urls import path, include

from .views import home_view, about_view, pw_protected_view, user_only_view, staff_only_view
from auth.views import register_view

urlpatterns = [
    path("", home_view, name= "home"),
    path("protected/",pw_protected_view),
    path("protected/user-only",user_only_view),
    path("protected/staff-only",staff_only_view),
    path("about/", about_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),
    path('register/', register_view),
    
]
