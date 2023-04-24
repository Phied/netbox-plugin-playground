from extras.plugins import PluginConfig

class NetboxBgpPlaygroundConfig(PluginConfig):
    name =  'netbox-bgp-playground'
    verbose_name = 'Netbox BGP Playground'
    description = 'Manage BGP Stuffs'
    version =  '0.01'
    base_url = 'bgp-playground'

config = NetboxBgpPlaygroundConfig