from netbox.views import generic
from . import forms, models, tables, filtersets
from django.db.models import Count

# Need to create 4 views at minimum: detail, list, edit, delete

# Regular communities here!
# Create detail view
class BgpCommunityView(generic.ObjectView):
    queryset = models.BgpCommunity.objects.all()

# Create list view
class BgpCommunityListView(generic.ObjectListView):
    queryset = models.BgpCommunity.objects.all()
    table = tables.BgpCommunityTable

    # Added to create filter functionality
    filterset = filtersets.BgpCommunityFilterSet
    filterset_form = forms.BgpCommunityFilterForm

# Create edit view
class BgpCommunityEditView(generic.ObjectEditView):
    queryset = models.BgpCommunity.objects.all()
    form = forms.BgpCommunityForm
    default_return_url = "plugins:netbox_bgp:bgpcommunity_list"

# Bulk Edit View
class BgpCommunityBulkEditView(generic.BulkEditView):
    queryset = models.BgpCommunity.objects.all()
    filterset = filtersets.BgpCommunityFilterSet
    table = tables.BgpCommunityTable
    form = forms.BgpCommunityBulkEditForm

# Create import view - notice it's model_form and not form like the others
class BgpCommunityImportView(generic.BulkImportView):
    queryset = models.BgpCommunity.objects.all()
    model_form = forms.BgpCommunityImportForm
    table = tables.BgpCommunityTable
    default_return_url = "plugins:netbox_bgp:bgpcommunity_list"

# Create delete view
class BgpCommunityDeleteView(generic.ObjectDeleteView):
    queryset = models.BgpCommunity.objects.all()

# Create bulk delete view
class BgpCommunityBulkDeleteView(generic.BulkDeleteView):
    queryset = models.BgpCommunity.objects.all()
    table = tables.BgpCommunityTable
    default_return_url = "plugins:netbox_bgp:bgpcommunity_list"



# Community Groups here!
# Create detail view
class BgpCommunityGroupView(generic.ObjectView):
    queryset = models.BgpCommunityGroup.objects.all()

    # Need to add this function to call it in our template later on so we get a list of the communities on the parent
    def get_extra_context(self, request, instance):       
        table = tables.BgpCommunityTable(instance.communities.all())
        table.configure(request)

        return {
            'communities_table': table
        }

# Create list view
class BgpCommunityGroupListView(generic.ObjectListView):
    #queryset = models.BgpCommunityGroup.objects.all()
    queryset = models.BgpCommunityGroup.objects.annotate(
        community_count=Count('communities')
    )
    table = tables.BgpCommunityGroupTable

    # Added to create filter functionality
    filterset = filtersets.BgpCommunityGroupFilterSet
    filterset_form = forms.BgpCommunityGroupFilterForm

# Create edit view
class BgpCommunityGroupEditView(generic.ObjectEditView):
    queryset = models.BgpCommunityGroup.objects.all()
    form = forms.BgpCommunityGroupForm
    default_return_url = "plugins:netbox_bgp:bgpcommunitygroup_list"

# Create import view - notice it's model_form and not form like the others
class BgpCommunityGroupImportView(generic.BulkImportView):
    queryset = models.BgpCommunityGroup.objects.all()
    model_form = forms.BgpCommunityGroupImportForm
    table = tables.BgpCommunityGroupTable
    default_return_url = "plugins:netbox_bgp:bgpcommunitygroup_list"

# Bulk Edit View
class BgpCommunityGroupBulkEditView(generic.BulkEditView):
    queryset = models.BgpCommunityGroup.objects.all()
    filterset = filtersets.BgpCommunityGroupFilterSet
    table = tables.BgpCommunityGroupTable
    form = forms.BgpCommunityGroupBulkEditForm


# Create delete view
class BgpCommunityGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.BgpCommunityGroup.objects.all()
    default_return_url = "plugins:netbox_bgp:bgpcommunitygroup_list"

# Create bulk delete view
class BgpCommunityGroupBulkDeleteView(generic.BulkDeleteView):
    queryset = models.BgpCommunityGroup.objects.all()
    table = tables.BgpCommunityGroupTable
    default_return_url = "plugins:netbox_bgp:bgpcommunitygroup_list"