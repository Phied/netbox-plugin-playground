import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BgpCommunity


# This is basically how our netbox orders the page when viewing it - it's a table structure.
class BgpCommunityTable(NetBoxTable):
    
    # Overwrite fields information below based on these values:
    status = ChoiceFieldColumn()
    
    name = tables.Column(
        linkify=True
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
        fields = ('pk','name', 'community','description', 'status', 'tenant', 'id', 'actions')
        default_columns = ('name', 'community', 'description', 'status', 'tenant', 'actions')