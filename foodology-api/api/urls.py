from django.urls import path, include
from rest_framework import routers

from meals.views import IngredientsViewSet

router = routers.DefaultRouter()
router.register('ingredients', IngredientsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]