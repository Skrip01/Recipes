from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import RecipeViewSet, CommentViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
