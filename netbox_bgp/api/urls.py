from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_bgp'

router = NetBoxRouter()
router.register('bgp-communities', views.BgpCommunityViewSet)

urlpatterns = router.urls