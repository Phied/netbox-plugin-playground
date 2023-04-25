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


# Query stuff here
class Query(ObjectType):
    bgpcommunity = ObjectField(BgpCommunityType)
    bgpcommunity_list = ObjectListField(BgpCommunityType)


schema = Query
