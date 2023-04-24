from extras.plugins import PluginConfig

class BgpConfig(PluginConfig):
    name =  'netbox_bgp'
    verbose_name = 'Netbox BGP Playground'
    description = 'Manage BGP Stuffs'
    version =  '0.01'
    base_url = 'bgp'

config = BgpConfig