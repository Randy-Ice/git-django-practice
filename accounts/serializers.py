from django.contrib.auth.models import AbstractUser
from djoser.serializers import UserCreatePasswordRetypeSerializer

class CustomRegistrationRetypePasswordSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]