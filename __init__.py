from extras.plugins import PluginConfig

class NetboxBGP(PluginConfig):
    name =  'netbox_bgp_playground'
    verbose_name = 'Netbox BGP Playground'
    description = 'Manage BGP Stuffs'
    version =  '0.01'
    base_url = 'bgp-playground'
    min_version = '3.4.0'

config = NetboxBGPConfig