from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^', include('project.apps.tasks.urls')),
    url(r'^', include('project.apps.users.urls')),
    url(r'^', include('project.apps.organizations.urls')),
]
