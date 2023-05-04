from django.urls import path
from . import models, views

from netbox.views.generic import ObjectChangeLogView

urlpatterns = [

    # Community urls
    path('bgp-communities/', views.BgpCommunityListView.as_view(), name='bgpcommunity_list'),
    path('bgp-communities/add/', views.BgpCommunityEditView.as_view(), name='bgpcommunity_add'),
    #path('bgp-communities/import/', views.BgpCommunityImportView.as_view(), name='bgpcommunity_import'),
    path('bgp-communities/<int:pk>/', views.BgpCommunityView.as_view(), name='bgpcommunity'),
    path('bgp-communities/edit/', views.BgpCommunityBulkEditView.as_view(), name='bgpcommunity_bulk_edit'),
    path('bgp-communities/<int:pk>/edit/', views.BgpCommunityEditView.as_view(), name='bgpcommunity_edit'),
    path('bgp-communities/delete/', views.BgpCommunityBulkDeleteView.as_view(), name='bgpcommunity_bulk_delete'),
    path('bgp-communities/<int:pk>/delete/', views.BgpCommunityDeleteView.as_view(), name='bgpcommunity_delete'),
    path('bgp-communities/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bgpcommunity_changelog', kwargs={
        'model': models.BgpCommunity
    }),

    # BGP Community Group urls
    path('bgp-community-group/', views.BgpCommunityGroupListView.as_view(), name='bgpcommunitygroup_list'),
    path('bgp-community-group/add/', views.BgpCommunityGroupEditView.as_view(), name='bgpcommunitygroup_add'),
    path('bgp-community-group/<int:pk>/', views.BgpCommunityGroupView.as_view(), name='bgpcommunitygroup'),
    path('bgp-community-group/edit/', views.BgpCommunityGroupBulkEditView.as_view(), name='bgpcommunitygroup_bulk_edit'),
    path('bgp-community-group/<int:pk>/edit/', views.BgpCommunityGroupEditView.as_view(), name='bgpcommunitygroup_edit'),
    path('bgp-community-group/delete/', views.BgpCommunityGroupBulkDeleteView.as_view(), name='bgpcommunitygroup_bulk_delete'),
    path('bgp-community-group/<int:pk>/delete/', views.BgpCommunityGroupDeleteView.as_view(), name='bgpcommunitygroup_delete'),
    path('bgp-community-group/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bgpcommunitygroup_changelog', kwargs={
        'model': models.BgpCommunityGroup
    }),

]
