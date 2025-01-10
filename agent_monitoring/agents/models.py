from django.db import models
import uuid


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_address = models.GenericIPAddressField(unique=True)
    asn = models.CharField(max_length=100, blank=True, null=True)
    isp = models.CharField(max_length=100, blank=True, null=True)
    last_reported = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agent {self.ip_address} - ASN: {self.asn}, ISP: {self.isp}"
