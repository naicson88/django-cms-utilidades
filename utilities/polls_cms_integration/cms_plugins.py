from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import PollPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel  # model where plugin data are saved
    module = _("Polls")
    name = _("0000 - Poll Plugin")  # name of the plugin in the interface
    render_template = "poll_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context