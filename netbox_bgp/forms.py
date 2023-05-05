from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm, NetBoxModelImportForm
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField, CSVChoiceField, CSVModelChoiceField
from tenancy.models import Tenant
from dcim.models import Device
from django.core.validators import RegexValidator
from .models import BgpCommunity, BgpCommunityGroup, ActionChoices

from django import forms

# Create normal form
class BgpCommunityForm(NetBoxModelForm):
    # Replaces tenant below with what netbox has for tenants
    parentgroup = DynamicModelMultipleChoiceField(queryset=BgpCommunityGroup.objects.all(), required=False, label="Parent Community Group(s)")
    devices_list = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False, label="Device(s)")

    class Meta:
        model = BgpCommunity
        fields = ('name', 'community', 'parentgroup', 'devices_list', 'description', 'status')

# Our Import form
class BgpCommunityImportForm(NetBoxModelImportForm):
    #Unable to import these at current.  Netbox freaks out on CSV with many-many field types
    #parentgroup = DynamicModelMultipleChoiceField(queryset=BgpCommunityGroup.objects.all(), required=False, label="Parent communities that have this as a child.")
    #devices_list = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False, label="Device(s) community has been configured on")
    status = forms.CharField(max_length=30, required=False, help_text="Options are Active or Depricated")
    name = forms.CharField(help_text="Name to identify community")
    community = forms.CharField(help_text="Community String in community syntax.  Ex: 65000:001")
    description = forms.CharField(required=False, help_text="Brief description of what the community is used for.")

    class Meta:
        model = BgpCommunity
        fields = ('name', 'community', 'status', 'description')
    

# Our bulk edit form!
class BgpCommunityBulkEditForm(NetBoxModelBulkEditForm):
    #pk = forms.ModelChoiceField(
    #    queryset=BgpCommunity.objects.all(),
    #    widget=forms.MultipleHiddenInput
    #)

    parentgroup = DynamicModelMultipleChoiceField(queryset=BgpCommunityGroup.objects.all(), required=False, label="Parent Community Group(s)")
    devices_list = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False, label="Device(s)")
    status = forms.ChoiceField(
        required=False,
        choices=ActionChoices
    )

    model = BgpCommunity
    nullable_fields = [
        'status','devices_list','parentgroup'
    ]

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


# BGP Community Group Form Stuff below!

# Create bgpcommunitygroup form!
class BgpCommunityGroupForm(NetBoxModelForm):
    #devices = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    devices_list = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False, label="Device(s)")
    #community_children = DynamicModelMultipleChoiceField(queryset=BgpCommunity.objects.all, required=False, label="Child Community(s)")

    class Meta:
        model = BgpCommunityGroup
        fields = ('name','description','devices_list','comments','tags')

# Our bulk edit form!
class BgpCommunityGroupBulkEditForm(NetBoxModelBulkEditForm):

    devices_list = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False, label="Device(s)")

    model = BgpCommunityGroup
    nullable_fields = [
        'devices_list'
    ]

# Create bgp filter form!
class BgpCommunityGroupFilterForm(NetBoxModelFilterSetForm):
    model = BgpCommunityGroup

    bgpcommunity_group = forms.ModelMultipleChoiceField(
        queryset=BgpCommunityGroup.objects.all(),
        required=False,
        label="BGP Community Group"
    )

# Our Import form
class BgpCommunityGroupImportForm(NetBoxModelImportForm):

    name = forms.CharField(help_text="Name to identify community")
    description = forms.CharField(required=False, help_text="Brief description of what the community is used for.")

    class Meta:
        model = BgpCommunityGroup
        fields = ('name', 'description')
    