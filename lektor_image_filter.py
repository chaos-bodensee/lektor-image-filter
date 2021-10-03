# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.context import get_ctx

def cfg():
    ctx = get_ctx()
    plugin = ctx.env.plugins["image-resize"]
    config = plugin.config
    return config

def create_src_html(fileprefix, config):
    returnvalue = ''
    index = 0
    for name, size in config:
        width = int(size.get("max_width", "0"))
        if width > 1:
            if index < 1:
                returnvalue = str(returnvalue) + 'src="' + str(fileprefix) + '-' + str(name) + '.webp" width="' + str(width) + '" '
            index =+ 1
    return str(returnvalue)
#        for item, conf in config.items():
#            width = int(conf["max_width"])
#            height = int(conf.get("max_height", "0"))


def image_filter(inputstring):
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    src_html = create_src_html(fileprefix, config.items())
    return str(inputstring + "foo" + str(src_html) + 'ˍ| ' + str(list(config.items())[0]))

class ImageFilterPlugin(Plugin):
    name = 'image-filter'
    description = u'A filter to print the input image in different predefined image sizes.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['webpimagesizes'] = image_filter

#            <img src="{{ image }}" width="{{ image.width / 2 | int }}"
#              srcset="
#          <img src="waffle-small.webp"
#            srcset="waffle-small.webp  512w,   // Viewport bis zu 512
#            waffle-medium.webp 900w,   // Viewport größer als 512
#            waffle-woowee.webp 1440w"  // Viewport größer als 900
#  />

