# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.context import get_ctx

def cfg():
    ctx = get_ctx()
    plugin = ctx.env.plugins["image-resize"]
    config = plugin.config
    return config

def get_width(inputstring, size):
    '''
      return width for first row where width > 1
      Calculate width if no one is defined in config and image is lektor.db.Image.
    '''
    width = int(size.get("max_width", "0"))
    if width > 1:
        if str(type(inputstring)) == "<class 'lektor.db.Image'>":
            height = int(size.get("max_height", "0"))
            if height > 1:
                src_width = inputstring.width
                src_height = inputstring.width
                computed_width = height * (src_width / src_height)
                return int(computed_width)
            else:
                return int(width)
        else:
            return int(width)

def get_height(inputstring, size):
    '''
      return height for first row where width > 1
      Calculate height if no one is defined in config and image is lektor.db.Image
    '''
    height = int(size.get("max_height", "0"))
    width = int(size.get("max_width", "0"))
    if width > 1:
        if height > 1:
            return int(height)
        else:
            if str(type(inputstring)) == "<class 'lektor.db.Image'>":
                src_width = inputstring.width
                src_height = inputstring.height
                computed_height = width * (src_height / src_width)
                return int(computed_height)
            else:
                return int(height)
    else:
        return int(height)

def create_src_html(inputstring, fileprefix, config, filesuffix):
    '''
      Return first filename with width > 1
    '''
    returnvalue = ''
    index = 0
    for name, size in config:
        width = int(get_width(inputstring, size))
        if width > 1:
            if index < 1:
                returnvalue = str(fileprefix) + "-" + str(name) + str(filesuffix)
            index =+ 1
    return str(returnvalue)

def create_width_html(inputstring, config):
    '''
      return first width > 1
    '''
    returnvalue = ''
    index = 0
    for name, size in config:
        width = int(get_width(inputstring, size))
        if width > 1:
            if index < 1:
                returnvalue = str(width)
            index =+ 1
    return str(returnvalue)

def create_height_html(inputstring, config):
    '''
      return first height > 1
    '''
    returnvalue = ''
    index = 0
    for name, size in config:
        height = int(get_height(inputstring, size))
        if height > 1:
            if index < 1:
                returnvalue = str(height)
            index =+ 1
    return str(returnvalue)

def create_srcset_html(inputstring, fileprefix, config, filesuffix):
    '''
      return srcset including width
    '''
    returnvalue = ''
    returnlist = []
    for name, size in config:
        width = int(get_width(inputstring, size))
        if width > 1:
            returnlist.append(f"{ fileprefix }-{ name }{ filesuffix } { width }w")
    return str(', '.join(returnlist))

def get_fileprefix(inputstring):
    '''
      return file prefix
    '''
    file_src_string = ''
    if str(type(inputstring)) == "<class 'lektor.db.Image'>":
        file_src_string = str(inputstring.path)
    else:
        file_src_string = str(inputstring)
    ext_pos = file_src_string.rfind('.')
    fileprefix = str(file_src_string[:ext_pos])
    return str(fileprefix)

def webp_image_filter_src(inputstring):
    '''
      Return full first filename as webp with width > 1
    '''
    filesuffix = '.webp'
    fileprefix = get_fileprefix(inputstring)
    config = cfg()
    src_html = create_src_html(inputstring, fileprefix, config.items(), filesuffix)
    return str(src_html)

def image_filter_width(inputstring):
    config = cfg()
    width_html = create_width_html(inputstring, config.items())
    return str(width_html)

def image_filter_height(inputstring):
    config = cfg()
    height_html = create_height_html(inputstring, config.items())
    return str(height_html)

def webp_image_filter_srcset(inputstring):
    '''
      Return srcset as webp
    '''
    filesuffix = '.webp'
    fileprefix = get_fileprefix(inputstring)
    config = cfg()
    srcset_html = create_srcset_html(inputstring, fileprefix, config.items(), filesuffix)
    return str(srcset_html)

def jpg_image_filter_src(inputstring):
    filesuffix = '.jpg'
    fileprefix = get_fileprefix(inputstring)
    config = cfg()
    src_html = create_src_html(inputstring, fileprefix, config.items(), filesuffix)
    return str(src_html)

def jpg_image_filter_srcset(inputstring):
    filesuffix = '.jpg'
    fileprefix = get_fileprefix(inputstring)
    config = cfg()
    srcset_html = create_srcset_html(inputstring, fileprefix, config.items(), filesuffix)
    return str(srcset_html)

class ImageFilterPlugin(Plugin):
    name = 'image-filter'
    description = u'A filter to print the input image in different predefined image sizes.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['imagessrcsetwebp'] = webp_image_filter_srcset
        self.env.jinja_env.filters['imagessrcwebp'] = webp_image_filter_src
        self.env.jinja_env.filters['imagessrcsetjpg'] = jpg_image_filter_srcset
        self.env.jinja_env.filters['imagessrcjpg'] = jpg_image_filter_src
        self.env.jinja_env.filters['firstwidth'] = image_filter_width
        self.env.jinja_env.filters['firstheight'] = image_filter_height
