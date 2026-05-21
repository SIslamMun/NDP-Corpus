import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def jupyterhub_endpoint():
    value = toolkit.config.get('ckanext.ndp.jupyterhub_endpoint')
    return value

class NdpPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "ndp")

    # ITemplateHelpers
    def get_helpers(self):
        return {'ndp_jupyterhub_endpoint': jupyterhub_endpoint}
