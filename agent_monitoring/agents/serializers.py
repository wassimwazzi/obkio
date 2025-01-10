from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ["id", "ip_address", "asn", "isp", "last_reported"]
        read_only_fields = ["id", "asn", "isp", "last_reported"]
