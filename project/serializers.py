from rest_framework import serializers

from .models import Project


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'user', 'name', 'type', 'status', 'is_done', 'started', 'finished', 'created', 'updated',
            'user_name', 'type_name'
        )

    def create(self, validated_data):
        print("CREATE")
        print(validated_data)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("UPDATE")
        print(instance)
        print(validated_data)

        return super().update(instance, validated_data)
