from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelChoiceField
from tenancy.models import Tenant
from .models import BgpCommunity, ActionChoices

from django import forms

class BgpCommunityForm(NetBoxModelForm):
    # Replaces tenant below with what netbox has for tenants
    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=False)

    class Meta:
        model = BgpCommunity
        fields = ('name', 'community', 'description', 'status', 'tenant')

# Created to enable filtering on fields!
class BgpCommunityFilterForm(NetBoxModelFilterSetForm):
    model = BgpCommunity
    bgpcommunity_list = forms.ModelMultipleChoiceField(
        queryset=BgpCommunity.objects.all(),
        required=False
    )

    action = forms.MultipleChoiceField(
        choices=ActionChoices,
        required=False
    )