from django.conf.urls import url

from project.apps.tasks.views import ApiTaskListView, ApiTaskDetailView

urlpatterns = [
    url(r'^api/tasks/$', ApiTaskListView.as_view()),
    url(r'^api/tasks/(?P<pk>\d+)/$', ApiTaskDetailView.as_view()),
]
