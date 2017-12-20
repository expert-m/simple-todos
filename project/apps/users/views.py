from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from project.apps.users.serializers import LoginSerializer


class ApiLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        pass

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        user.active_organization_id = serializer.validated_data[
            'organization_id']
        user.save(update_fields=['active_organization'])

        login(request, user)

        return Response(serializer.data, status=status.HTTP_200_OK)
