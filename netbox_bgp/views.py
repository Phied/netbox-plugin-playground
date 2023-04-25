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

