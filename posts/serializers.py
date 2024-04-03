from rest_framework import serializers
from .models import CommunityPost


class CommunityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPost
        fields = ['username', 'profile_picture_url', 'caption']
