"""
NOTES:

- 
- Authentication is missing, anyone can create an agent.
"""

import requests
from rest_framework import viewsets
from .models import Agent
from .serializers import AgentSerializer


def get_ip_info(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    asn, isp = None, None
    if response.status_code == 200:
        data = response.json()
        asn_info = data.get("org", "")
        # Extract ASN number from the 'org' string (format: 'AS{ASN} {ISP}')
        asn = asn_info.split()[0] if asn_info.startswith("AS") else None
        isp = asn_info[len(asn) :].strip() if asn else None

    return asn, isp


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def perform_create(self, serializer):
        # Fetch ASN and ISP information for the IP address using an external API
        ip_address = serializer.validated_data["ip_address"]
        asn, isp = get_ip_info(ip_address)
        serializer.save(asn=asn, isp=isp)

    def perform_update(self, serializer):
        ip_address = serializer.validated_data.get("ip_address")
        agent = self.get_object()

        # Only fetch new ASN and ISP if the IP address has changed
        if ip_address != agent.ip_address:
            asn, isp = get_ip_info(ip_address)
            serializer.save(asn=asn, isp=isp)
        else:
            # If the IP address hasn't changed, no need to update ASN/ISP
            serializer.save()
