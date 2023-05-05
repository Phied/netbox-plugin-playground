from extras.plugins import PluginConfig

class BgpConfig(PluginConfig):
    name =  'netbox_bgp'
    verbose_name = 'Netbox BGP'
    description = 'A way to manage Netbox BGP Attributes'
    author = 'Keith Perkins'
    author_email = 'keithaperkins@gmail.com'
    version =  'v0.0.1beta'
    base_url = 'bgp'

config = BgpConfig