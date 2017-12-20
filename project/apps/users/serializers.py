from django.contrib.auth import authenticate
from rest_framework import serializers

from project.apps.organizations.models import Organization


class LoginSerializer(serializers.Serializer):
    organization_id = serializers.IntegerField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_organization_id(self, value):
        organization = Organization.objects.filter(id=value).first()

        if not organization:
            raise serializers.ValidationError(
                'This organization does not exist.')

        return value

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])

        if user is None:
            raise serializers.ValidationError(
                'Check your email address and password.')

        if not user.organizations.filter(id=attrs['organization_id']).exists():
            raise serializers.ValidationError(
                'This organization does not have this user.')

        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
