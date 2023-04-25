from netbox.models import NetBoxModel
from django.db import models
from utilities.choices import ChoiceSet


class ActionChoices(ChoiceSet):
    key = 'BgpCommunity.status'

    CHOICES = [
        ('enabled', 'Enabled', 'green'),
        ('disabled', 'Disabled', 'red'),
        ('reserved', 'Reserved', 'yellow')
    ]

class BgpCommunity(NetBoxModel):
    index = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=30, choices=ActionChoices, null=False, blank=False)
    tenant = models.ForeignKey(to='tenancy.Tenant', on_delete=models.PROTECT, related_name='+', blank=True, null=True)

class Meta:
    ordering = ('name', 'index')
    unique_together = ('name', 'index')

def get_status_color(self):
    return ActionChoices.colors.get(self.status)
