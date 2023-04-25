from django.urls import path
from . import models, views

from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    # Community urls
    path('bgp-communities/', views.BgpCommunityListView.as_view(), name='bgpcommunity_list'),
    path('bgp-communities/add/', views.BgpCommunityEditView.as_view(), name='bgpcommunity_add'),
    path('bgp-communities/<int:pk>/', views.BgpCommunityView.as_view(), name='bgpcommunity'),
    path('bgp-communities/<int:pk>/edit/', views.BgpCommunityEditView.as_view(), name='bgpcommunity_edit'),
    path('bgp-communities/<int:pk>/delete/', views.BgpCommunityDeleteView.as_view(), name='bgpcommunity_delete'),
    path('bgp-communities/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bgpcommunity_changelog', kwargs={
        'model': models.BgpCommunity
    }),

)
