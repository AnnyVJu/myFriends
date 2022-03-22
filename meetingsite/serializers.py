from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from meetingsite.models import Profile, Post, Comment

UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'city', 'birth_date', 'gender', 'relationship']


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']


class PostSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        exclude = []


class CommentSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        exclude = ['post']
