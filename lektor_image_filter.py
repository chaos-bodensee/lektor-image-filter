# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.context import get_ctx

def cfg():
    ctx = get_ctx()
    plugin = ctx.env.plugins["image-resize"]
    config = plugin.config
    return config

def create_src_html(fileprefix, config, filesuffix):
    returnvalue = ''
    index = 0
    for name, size in config:
        width = int(size.get("max_width", "0"))
        if width > 1:
            if index < 1:
                returnvalue = str(returnvalue) + 'src="' + str(fileprefix) + '-' + str(name) + str(filesuffix) + '" width="' + str(width) + '" '
            index =+ 1
    return str(returnvalue)

def create_srcset_html(fileprefix, config, filesuffix):
    returnvalue = 'srcset="'
    for name, size in config:
        width = int(size.get("max_width", "0"))
        if width > 1:
            returnvalue = str(returnvalue) + str(fileprefix) + '-' + str(name) + str(filesuffix) + ' ' + str(width) + 'w, '
    returnvalue = str(returnvalue) + '"'
    return str(returnvalue)

def webp_image_filter(inputstring):
    filesuffix = '.webp'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    src_html = create_src_html(fileprefix, config.items(), filesuffix)
    srcset_html = create_srcset_html(fileprefix, config.items(), filesuffix)
    return str( str(src_html) + str(srcset_html) )

def jpg_image_filter(inputstring):
    filesuffix = '.jpg'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    src_html = create_src_html(fileprefix, config.items(), filesuffix)
    srcset_html = create_srcset_html(fileprefix, config.items(), filesuffix)
    return str( str(src_html) + str(srcset_html) )

class ImageFilterPlugin(Plugin):
    name = 'image-filter'
    description = u'A filter to print the input image in different predefined image sizes.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['webpimagesizes'] = webp_image_filter
        self.env.jinja_env.filters['jpgimagesizes'] = jpg_image_filter
