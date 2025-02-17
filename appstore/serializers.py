from rest_framework import serializers
from appstore.models import App


class AppSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = App
        fields = ['id', 'title', 'description', 'price', 'owner', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
