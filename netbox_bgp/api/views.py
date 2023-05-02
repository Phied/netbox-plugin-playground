from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import BgpCommunitySerializer, BgpCommunityGroupSerializer

class BgpCommunityViewSet(NetBoxModelViewSet):
    queryset = models.BgpCommunity.objects.prefetch_related(
        'tags'
    )
    serializer_class = BgpCommunitySerializer
    filterset_class = filtersets.BgpCommunityFilterSet

class BgpCommunityGroupViewSet(NetBoxModelViewSet):
    queryset = models.BgpCommunityGroup.objects.prefetch_related(
        'tags'
    )

    serializer_class = BgpCommunityGroupSerializer
    filterset_class = filtersets.BgpCommunityGroupFilterSet
