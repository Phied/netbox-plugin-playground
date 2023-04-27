from netbox.filtersets import NetBoxModelFilterSet
from .models import BgpCommunity, BgpCommunityGroup

class BgpCommunityFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = BgpCommunity
        fields = ('name', 'community', 'parentgroup', 'description', 'status', 'tenant')

        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)
        

class BgpCommunityGroupFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = BgpCommunityGroup
        fields = ('name', 'description', 'devices')

        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)