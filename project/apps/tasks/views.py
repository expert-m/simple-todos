from rest_framework import permissions, mixins, generics

from project.apps.tasks.models import Task
from project.apps.tasks.serializers import TaskEditSerializer, \
    TaskListSerializer, TaskDetailSerializer


class ApiTaskListView(mixins.ListModelMixin, mixins.CreateModelMixin,
                      generics.GenericAPIView):
    serializer_class = TaskEditSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(
            organization=self.request.user.active_organization
        ).order_by('created_at')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskListSerializer

        return self.serializer_class

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            organization=self.request.user.active_organization
        )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApiTaskDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = TaskEditSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(
            organization=self.request.user.active_organization
        ).order_by('created_at')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskDetailSerializer

        return self.serializer_class

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(
            user=self.request.user,
            organization=self.request.user.active_organization
        )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
