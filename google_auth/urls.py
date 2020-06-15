from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('profile_app.urls')),
]

handler404 = 'profile_app.views.not_found'
