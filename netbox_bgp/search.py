from netbox.search import SearchIndex, register_search
from .models import BgpCommunity, BgpCommunityGroup

# When modifying don't forget to reindex!  Objects created after will be indexed automatically
# manage.py reindex netbox_bgp

#Register class
@register_search
class BgpCommunityIndex(SearchIndex):
    model = BgpCommunity

    # Only put the fields you actually care to search with.  Closer to 0 is higher.
    fields = (
        ('name', 100),
        ('community', 100),
    )

@register_search
class BgpCommunityGroupIndex(SearchIndex):
    model = BgpCommunityGroup

    # Fields we care about searching for:
    fields = (
        ('name', 100),
    )