from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'avatar',
            'phone',
            'telegram',
            'whatsapp',
            'behance',
            'instagram',
        ]

