from extras.plugins import PluginConfig

class NetboxBgpPlayground(PluginConfig):
    name =  'netbox-bgp-playground'
    verbose_name = 'Netbox BGP Playground'
    description = 'Manage BGP Stuffs'
    version =  '0.01'
    base_url = 'bgp-playground'

config = NetboxBgpPlayground