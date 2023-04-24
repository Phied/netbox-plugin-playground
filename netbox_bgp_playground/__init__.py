from extras.plugins import PluginConfig

class NetboxPluginPlaygroundConfig(PluginConfig):
    name =  'netbox_plugin_playground'
    verbose_name = 'Netbox BGP Playground'
    description = 'Manage BGP Stuffs'
    version =  '0.01'
    base_url = 'netbox-bgp-playground'
    min_version = '3.4.0'

config = NetboxPluginPlaygroundConfig