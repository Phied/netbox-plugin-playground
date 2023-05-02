from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


# Object Types here
class BgpCommunityType(NetBoxObjectType):

    class Meta:
        model = models.BgpCommunity
        fields = '__all__'
        filterset_class = filtersets.BgpCommunityFilterSet


class BgpCommunityGroupType(NetBoxObjectType):

    class Meta:
        model = models.BgpCommunityGroup
        fields = '__all__'
        filterset_class = filtersets.BgpCommunityGroupFilterSet


# Query stuff here
class Query(ObjectType):
    bgpcommunity = ObjectField(BgpCommunityType)
    bgpcommunity_list = ObjectListField(BgpCommunityType)

    bgpcommunitygroup = ObjectField(BgpCommunityGroupType)
    bgpcommunitygroup_list = ObjectListField(BgpCommunityGroupType)


schema = Query
