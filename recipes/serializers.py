from rest_framework import serializers
from .models import Recipe, Comment, Rating


class RecipeSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'created_at', 'image', 'average_rating']

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            total = sum(r.value for r in ratings)
            return total / ratings.count()
        return None


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'author', 'author_username', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'author', 'value', 'created_at']
        read_only_fields = ['author', 'created_at']
