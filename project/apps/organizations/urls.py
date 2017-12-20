from django.conf.urls import url

from project.apps.organizations.views import ApiOrganizationListView

urlpatterns = [
    url(r'^api/organizations/$', ApiOrganizationListView.as_view()),
]
