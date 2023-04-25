from netbox.filtersets import NetBoxModelFilterSet
from .models import BgpCommunity

class BgpCommunityFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = BgpCommunity
        fields = ('name', 'community', 'description', 'status', 'tenant')

        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)