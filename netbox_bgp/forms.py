from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from tenancy.models import Tenant
from dcim.models import Device
from .models import BgpCommunity, BgpCommunityGroup, ActionChoices

from django import forms

# Create normal form
class BgpCommunityForm(NetBoxModelForm):
    # Replaces tenant below with what netbox has for tenants
    #tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=False)
    parentgroup = DynamicModelMultipleChoiceField(queryset=BgpCommunityGroup.objects.all(), label="Parent Community Group(s)")

    class Meta:
        model = BgpCommunity
        fields = ('name', 'community', 'parentgroup', 'description', 'status')

# Created to enable filtering on fields!
class BgpCommunityFilterForm(NetBoxModelFilterSetForm):
    model = BgpCommunity
    bgpcommunity_list = forms.ModelMultipleChoiceField(
        queryset=BgpCommunity.objects.all(),
        required=False,
        label="Community"
    )

    action = forms.MultipleChoiceField(
        choices=ActionChoices,
        required=False
    )

# Create bgpcommunitygroup form!
class BgpCommunityGroupForm(NetBoxModelForm):
    #devices = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    devices_list = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False, label="Device(s)")
    #community_children = DynamicModelMultipleChoiceField(queryset=BgpCommunity.objects.all, required=False, label="Child Community(s)")

    class Meta:
        model = BgpCommunityGroup
        fields = ('name','description','devices_list','comments','tags')


# Create bgp filter form!
class BgpCommunityGroupFilterForm(NetBoxModelFilterSetForm):
    model = BgpCommunityGroup

    bgpcommunity_group = forms.ModelMultipleChoiceField(
        queryset=BgpCommunityGroup.objects.all(),
        required=False,
        label="BGP Community Group"
    )