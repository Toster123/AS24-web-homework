from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'likes_count', 'comments_count', 'author', 'created_at')
        read_only_fields = ('author',)