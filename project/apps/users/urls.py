from django.conf.urls import url

from project.apps.users.views import ApiLoginView

urlpatterns = [
    url(r'^api/auth/$', ApiLoginView.as_view()),
]
