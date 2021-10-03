# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.context import get_ctx

def cfg():
    ctx = get_ctx()
    plugin = ctx.env.plugins["image-resize"]
    config = plugin.config
    return config


#        for item, conf in config.items():
#            width = int(conf["max_width"])
#            height = int(conf.get("max_height", "0"))


def image_filter(inputstring):
    config = cfg()
    return str(inputstring + "foo" + str(config.items()))

class ImageFilterPlugin(Plugin):
    name = 'image-filter'
    description = u'A filter to print the input image in different predefined image sizes.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['webpimagesizes'] = image_filter

