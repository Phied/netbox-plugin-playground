import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BgpCommunity, BgpCommunityGroup

# Create some labels to link to our many-to-many objects on our page rendereing
COL_DEVICES = """
 {% for device in value.all %}
    <a href="{{ device.get_absolute_url }}">{{ device }}</a>{% if not forloop.last %}<br />{% endif %}
 {% empty %}
    &mdash;
 {% endfor %}
"""

# Create some labels to link to our many-to-many objects on our page rendereing
COL_COMMUNITIES = """
 {% for community in value.all %}
    <a href="{{ community.get_absolute_url }}">{{ community }}</a>{% if not forloop.last %}<br />{% endif %}
 {% empty %}
    &mdash;
 {% endfor %}
"""

# Create the Group table
class BgpCommunityGroupTable(NetBoxTable):

    # Apply rendering template to our device column!
    devices_list = tables.TemplateColumn(
        template_code=COL_DEVICES
    )

    #Attempt to get count of communities under this group
    community_count = tables.Column(verbose_name="Community Count")

    # Create link for the Group name
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = BgpCommunityGroup

        fields = ('pk','name','description','community_count','devices_list','id','comments','actions')
        default_columns = ('name','description','community_count','devices_list')
        #fields = ('pk','name','description','devices_list','id','actions')
        #default_columns = ('name','description','devices')

# This is basically how our netbox orders the page when viewing it - it's a table structure.
class BgpCommunityTable(NetBoxTable):
    
    # Overwrite fields information below based on these values:
    status = ChoiceFieldColumn()
    
    name = tables.Column(
        linkify=True
    )

    parentgroup = tables.TemplateColumn(
        template_code=COL_COMMUNITIES
    )

    community = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = BgpCommunity
        # pk and actions columns render checkbox selectors for each row.
        fields = ('pk','name', 'parentgroup', 'community', 'description', 'status', 'id', 'actions')
        default_columns = ('name', 'community', 'parentgroup' 'description', 'status', 'actions')