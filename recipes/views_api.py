from rest_framework import viewsets, permissions
from .models import Recipe, Comment, Rating
from .serializers import RecipeSerializer, CommentSerializer, RatingSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-created_at')
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('-created_at')
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
