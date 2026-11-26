# responcible for registering a new user 
# takes user details from api request and validates them, saves in the db

from rest_framework import serializers
from django.contrib.auth import get_user_model

# storing the user model in a var
User = get_user_model()


# a class to tell django this is a serializer model
class UserRegistrationSerializer(serializers.ModelSerializer):

    # password must not be visible or fetched when asked user data and min 8 char
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    # this class tells what details should be considered
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'password'
        ]

    # after validation it creates var for all values from dict type and returnes
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)