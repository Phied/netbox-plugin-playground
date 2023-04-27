from netbox.views import generic
from . import forms, models, tables, filtersets

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

# Create list view
class BgpCommunityGroupListView(generic.ObjectListView):
    queryset = models.BgpCommunityGroup.objects.all()
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

