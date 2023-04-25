from extras.plugins import PluginConfig

class BgpConfig(PluginConfig):
    name =  'netbox_bgp'
    verbose_name = 'Netbox BGP'
    description = 'Beta to manage Netbox BGP Attributes'
    author = 'Keith Perkins'
    author_email = 'keithaperkins@gmail.com'
    version =  '0.01'
    base_url = 'bgp'

config = BgpConfig