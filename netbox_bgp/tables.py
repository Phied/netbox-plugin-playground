import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BgpCommunity, BgpCommunityGroup

# Create the Group table
class BgpCommunityGroupTable(NetBoxTable):

    # Attempt to get a count of the devices that have this in use
    devices = tables.Column()

    # Attempt to get count of communities under this group
    community_count = tables.Column()

    # Create link for the Group name
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = BgpCommunityGroup

        fields = ('pk','name','description','community_count','devices','id','actions')
        default_columns = ('name','description','community_count','devices')

# This is basically how our netbox orders the page when viewing it - it's a table structure.
class BgpCommunityTable(NetBoxTable):
    
    # Overwrite fields information below based on these values:
    status = ChoiceFieldColumn()
    
    name = tables.Column(
        linkify=True
    )

    parentgroup = tables.Column(
        linkify=True,
        
    )

    id = tables.Column(
        linkify=True
    )

    community = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = BgpCommunity
        # pk and actions columns render checkbox selectors for each row.
        fields = ('pk','name', 'parentgroup', 'community', 'description', 'status', 'tenant', 'id', 'actions')
        default_columns = ('name', 'community', 'parentgroup' 'description', 'status', 'tenant', 'actions')