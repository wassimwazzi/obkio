# Generated by Django 4.2.17 on 2025-01-10 18:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('asn', models.CharField(blank=True, max_length=100, null=True)),
                ('isp', models.CharField(blank=True, max_length=100, null=True)),
                ('last_reported', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
