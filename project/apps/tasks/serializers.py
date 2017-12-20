from rest_framework import serializers

from project.apps.tasks.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description',)


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'user_id',)


class TaskEditSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data['description']
        instance.save(update_fields=['description'])
        return instance
