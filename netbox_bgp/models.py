from netbox.models import NetBoxModel
from django.db import models
from utilities.choices import ChoiceSet
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class ActionChoices(ChoiceSet):
    key = 'BgpCommunity.status'

    CHOICES = [
        ('enabled', 'Enabled', 'green'),
        ('disabled', 'Disabled', 'red'),
        ('reserved', 'Reserved', 'yellow')
    ]

class BgpCommunity(NetBoxModel):
    name = models.CharField(max_length=100, blank=False)
    community = models.CharField(max_length=64, validators=[RegexValidator(r'\d+:\d+')], blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=30, choices=ActionChoices, null=False, blank=False)
    tenant = models.ForeignKey(to='tenancy.Tenant', on_delete=models.PROTECT, related_name='+', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Communities"
        ordering = ('community', 'id')

    def __str__(self):
        return self.community

    # Set the URL path as defined in urls.py for a single object view
    def get_absolute_url(self):
        return reverse('plugins:netbox_bgp:bgpcommunity', kwargs={'pk': self.pk})

    def get_status_color(self):
        return ActionChoices.colors.get(self.status)