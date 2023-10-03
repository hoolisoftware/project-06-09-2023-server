from rest_framework import serializers
from django.contrib.auth import get_user_model

from .. import models


User = get_user_model()


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    author = AuthorSerializer()

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'image', 'content', 'excerpt', 'categories', 'author', 'created'] # noqa
