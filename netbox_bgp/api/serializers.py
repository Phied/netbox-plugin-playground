from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import BgpCommunity

# Import serializer to grab tenant information from API since we reference it.  Without it, we'd only get ID
from tenancy.api.serializers import NestedTenantSerializer

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
            'id', 'display', 'url', 'name', 'community', 'description', 'status', 'tenant', 'tags', 'custom_fields', 'created', 'last_updated',
        )