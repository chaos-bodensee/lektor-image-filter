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
                returnvalue = str(fileprefix) + "-" + str(name) + str(filesuffix)
            index =+ 1
    return str(returnvalue)

def create_width_html(fileprefix, config, filesuffix):
    returnvalue = ''
    index = 0
    for name, size in config:
        width = int(size.get("max_width", "0"))
        if width > 1:
            if index < 1:
                returnvalue = str(width)
            index =+ 1
    return str(returnvalue)

def create_srcset_html(fileprefix, config, filesuffix):
    returnvalue = ''
    for name, size in config:
        width = int(size.get("max_width", "0"))
        if width > 1:
            returnvalue = str(returnvalue) + str(fileprefix) + "-" + str(name) + str(filesuffix) + " " + str(width) + "w, "
    return str(returnvalue)

def webp_image_filter_src(inputstring):
    filesuffix = '.webp'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    src_html = create_src_html(fileprefix, config.items(), filesuffix)
    return str(src_html)

def webp_image_filter_width(inputstring):
    filesuffix = '.webp'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    width_html = create_width_html(fileprefix, config.items(), filesuffix)
    return str(width_html)

def webp_image_filter_srcset(inputstring):
    filesuffix = '.webp'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    srcset_html = create_srcset_html(fileprefix, config.items(), filesuffix)
    return str(srcset_html)

def jpg_image_filter_src(inputstring):
    filesuffix = '.jpg'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    src_html = create_src_html(fileprefix, config.items(), filesuffix)
    return str(src_html)

def jpg_image_filter_width(inputstring):
    filesuffix = '.jpg'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    width_html = create_width_html(fileprefix, config.items(), filesuffix)
    return str(width_html)

def jpg_image_filter_srcset(inputstring):
    filesuffix = '.jpg'
    ext_pos = inputstring.rfind('.')
    fileprefix = str(inputstring[:ext_pos])
    config = cfg()
    srcset_html = create_srcset_html(fileprefix, config.items(), filesuffix)
    return str(srcset_html)

class ImageFilterPlugin(Plugin):
    name = 'image-filter'
    description = u'A filter to print the input image in different predefined image sizes.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['imagessrcsetwebp'] = webp_image_filter_srcset
        self.env.jinja_env.filters['imageswidthwebp'] = webp_image_filter_width
        self.env.jinja_env.filters['imagessrcwebp'] = webp_image_filter_src
        self.env.jinja_env.filters['imagessrcsetjpg'] = jpg_image_filter_srcset
        self.env.jinja_env.filters['imageswidthjpg'] = jpg_image_filter_width
        self.env.jinja_env.filters['imagessrcjpg'] = jpg_image_filter_src
