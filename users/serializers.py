from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import Account


class AccountRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Account
        fields = ('username',
                  'password',
                  'password2',)

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username'])
        if user:
            raise ValidationError({'Error': "username alreadt exists"})
        if attrs['password'] != attrs['password']:
            raise ValidationError({'Error': 'passwords did not match'})
        return attrs

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            password=make_password(validate_data['password']))

        account = Account.objects.create(
            user=user,
            username=validate_data['username']
        )

        return account

