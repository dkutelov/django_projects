from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timer_app.urls')),
    path('auth/', include('user_app.urls')),
]