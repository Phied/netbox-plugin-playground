from extras.plugins import PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices

communitylist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_bgp:bgpcommunity_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_bgp:bgpcommunity_list',
        link_text='BGP Communities',
        buttons=communitylist_buttons
    ),
)

