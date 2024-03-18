

from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

    def get_created_by(self, obj):
        return self.context['request'].user.username if self.context['request'].user.is_authenticated else None