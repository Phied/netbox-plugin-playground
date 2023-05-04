from netbox.models import NetBoxModel
from django.db import models
from utilities.choices import ChoiceSet
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class ActionChoices(ChoiceSet):
    key = 'BgpCommunity.status'

    CHOICES = [
        ('active', 'Active', 'green'),
        ('deprecated', 'Depricated', 'red')
    ]

class BgpCommunityGroup(NetBoxModel):
    name = models.CharField(max_length=100, blank=False)
    #Make this a many to many relationship to natvie "Device" field.
    devices_list = models.ManyToManyField(to='dcim.Device', verbose_name="Device List")
    description = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Community Groups"
        ordering = ('name', 'id')

    def __str__(self):
        return self.name
    
    # Set URL as defined in urls.py
    def get_absolute_url(self):
        return reverse('plugins:netbox_bgp:bgpcommunitygroup', kwargs={'pk': self.pk})

class BgpCommunity(NetBoxModel):
    #parentgroup = models.ForeignKey(to=BgpCommunityGroup,related_name='Group',on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Community Group")
    # Using related name here allow us to get the count later on by calling that name!
    parentgroup = models.ManyToManyField(to=BgpCommunityGroup, related_name='communities', blank=True, verbose_name="Parent Community Group(s)")
    name = models.CharField(max_length=100, blank=False)
    community = models.CharField(max_length=64, validators=[RegexValidator(r'\d+:\d+')], blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=30, choices=ActionChoices, null=False, blank=True)
    #tenant = models.ForeignKey(to='tenancy.Tenant', on_delete=models.PROTECT, related_name='+', blank=True, null=True)
    
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