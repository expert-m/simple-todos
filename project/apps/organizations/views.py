from rest_framework import permissions, generics

from project.apps.organizations.models import Organization
from project.apps.organizations.serializers import OrganizationSerializer


class ApiOrganizationListView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Organization.objects.order_by('name')
