from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import BgpCommunity, BgpCommunityGroup

# Import serializer to grab tenant information from API since we reference it.  Without it, we'd only get ID
from tenancy.api.serializers import NestedTenantSerializer

# Import serializer to grab device info
from dcim.api.serializers import NestedDeviceSerializer

# Create nested serializer here so the regular serializers can reference it later
class NestedBgpCommunitySerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_bgp-api:bgpcommunity-detail'
    )

    class Meta:
        model = BgpCommunity
        fields = ('id', 'url', 'display', 'name')


class BgpCommunitySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_bgp-api:bgpcommunity-detail'
    )

    # Use this to replace the tenant field below.  Without it, we'd only get an ID
    tenant = NestedTenantSerializer(required=False, allow_null=True)

    class Meta:
        model = BgpCommunity
        fields = (
            'id', 'display', 'url', 'name', 'community', 'parentgroup', 'description', 'status', 'tenant', 'tags', 'custom_fields', 'created', 'last_updated',
        )

# Create nested group serializer
class NestedBgpCommunityGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_bgp-api:bgpcommunitygroup-detail'
    )

    class Meta:
        model = BgpCommunityGroup
        fields = ('id','url','display','name')

# Create normal serializer for api
class BgpCommunityGroupSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_bgp-api:bgpcommunitygroup-detail'
    )
    
    # Modify device to use imported info above:
    devices = NestedDeviceSerializer(required=False, allow_null=True)

    class Meta:
        model = BgpCommunityGroup
        fields = (
            'id', 'display', 'url', 'name', 'devices', 'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )