from netbox.views import generic
from . import forms, models, tables, filtersets
from django.db.models import Count

# Need to create 4 views: detail, list, edit, delete

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

# Create delete view
class BgpCommunityDeleteView(generic.ObjectDeleteView):
    queryset = models.BgpCommunity.objects.all()




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

# Create delete view
class BgpCommunityGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.BgpCommunityGroup.objects.all()

