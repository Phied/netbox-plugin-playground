from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_bgp'

router = NetBoxRouter()

#Register each namespace???
router.register('bgp-communities', views.BgpCommunityViewSet)
router.register('bgp-community-groups', views.BgpCommunityGroupViewSet)

urlpatterns = router.urls