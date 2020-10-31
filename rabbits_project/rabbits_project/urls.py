from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def home_page(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='index'),
    path('quiz/', include('quiz_app.urls')),
    path('auth/', include('user_app.urls')),
]