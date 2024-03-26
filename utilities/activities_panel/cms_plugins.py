from cms.plugin_base import CMSPluginBase
from activities_panel.models import ActivitieModel, ActivitiesPanelModel
from django.utils.translation import gettext as _
from cms.plugin_pool import plugin_pool


@plugin_pool.register_plugin  # register the plugin
class ActivitiesPanelPlugin(CMSPluginBase):
    model = ActivitiesPanelModel  # model where plugin data are saved
    module = _("Activities")
    name = _("0001 - Activities Panel")  # name of the plugin in the interface
    render_template = "activities_panel.html"
    allow_children = True
    child_classes = ["ActivitiePlugin"]

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context

@plugin_pool.register_plugin
class ActivitiePlugin(CMSPluginBase):
    model = ActivitieModel
    module = _("Activities")
    name = _("Activitie")
    render_template = "activitie.html"
    require_parent = True
    parent_classes = ['ActivitiesPanelPlugin']
    
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        print(context)
        return context;