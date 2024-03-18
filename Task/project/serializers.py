
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']

    def get_created_by(self, obj):
        return self.context['request'].user.username if self.context['request'].user.is_authenticated else None