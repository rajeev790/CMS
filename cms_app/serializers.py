from rest_framework import serializers
from .models import User, Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post):
        return post.like_set.count()

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)
        self.fields['likes_count'] = serializers.SerializerMethodField()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'



# class PostSerializer(serializers.ModelSerializer):
#     likes_count = serializers.SerializerMethodField()

#     def get_likes_count(self, post):
#         return post.like_set.count()

#     class Meta:
#         model = Post
#         fields = '__all__'

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['likes_count'] = self.get_likes_count(instance)
#         return representation
