from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'recently password'}
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name',
        )
        write_only_fields = (
            'password',
            'password2',
        )
        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        if validated_data['password'] == validated_data['password2'] :
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )

            user.set_password(validated_data['password2'])
            user.save()

            return user
        else :
            raise serializers.ValidationError({"password": "password1 and password2 should be equal ."})