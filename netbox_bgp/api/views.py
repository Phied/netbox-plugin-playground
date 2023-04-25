from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import BgpCommunitySerializer

class BgpCommunityViewSet(NetBoxModelViewSet):
    queryset = models.BgpCommunity.objects.prefetch_related(
        'tenant','tags'
    )
    serializer_class = BgpCommunitySerializer
    filterset_class = filtersets.BgpCommunityFilterSet

