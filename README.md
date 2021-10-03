 image-filter
==============

[![PyPI version](https://badge.fury.io/py/lektor-image-filter.svg)](https://badge.fury.io/py/lektor-image-filter)
[![Downloads](https://pepy.tech/badge/lektor-image-filter)](https://pepy.tech/project/lektor-image-filter)
[![Linting Python package](https://github.com/chaos-bodensee/lektor-image-filter/actions/workflows/pythonpackage.yml/badge.svg)](https://github.com/chaos-bodensee/lektor-image-filter/actions/workflows/pythonpackage.yml)
[![Upload Python Package](https://github.com/chaos-bodensee/lektor-image-filter/actions/workflows/pythonpublish.yml/badge.svg)](https://github.com/chaos-bodensee/lektor-image-filter/actions/workflows/pythonpublish.yml)
[![MIT License](https://raw.githubusercontent.com/chaos-bodensee/lektor-image-filter/main/.github/license.svg?sanitize=true)](https://github.com/chaos-bodensee/lektor-image-filter/blob/main/LICENSE)

A [Lektor](https://getlektor.com) filter to print the input image in different predefined image sizes.

This plugin is designed to work together with the [lektor-image-resize](https://github.com/chaos-bodensee/lektor-image-resize) Plugin.

 Current Filters:
------------------
 + ``webpimagesizes`` will print the configured webp image sized based on the input file name.
 + ``jpgimagesizes`` will print the configured jpg image sized based on the input file name.

 Configuration
---------------
You can configure the image width in the config file called `configs/image-resize.ini` and add
a few sections for images. The section names can be whatever you want, the
final images will be called ``$(imagename)-$(sectionname).jpg`` and ``$(imagename)-$(sectionname).webp``.

If the ``max_width`` enty does not exist the entry will be ignored.

Here is a example config file:

```ini
[small]
max_width = 512

[medium]
max_width = 900
max_height = 900

[woowee]
max_width = 1440
```

 Example Output
----------------

### Lektor Jinja2 Input
```html
<img {{ 'waffle.jpg'|webpimagesizes }} />
```

### Lektor HTML Output:
```html
<img src="waffle-small.webp" width="512"
  srcset="waffle-small.webp  512w,
          waffle-medium.webp 900w,
          waffle-woowee.webp 1440w," />
```

 Installation
--------------
```bash
lektor plugin add lektor-image-filter
```
