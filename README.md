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
 + ``imagessrcsetwebp`` will print the configured sizes as ``webp`` to put in a ``srcset`` element.
 + ``imageswidthwebp`` will print the first configured ``webp`` image width to put in a ``width`` element.
 + ``imagessrcwebp`` will print the first configured ``webp`` image name to put in a ``src`` element.
 + ``imagessrcsetjpg`` will print the configured sizes as ``jpg`` to put in a ``srcset`` element.
 + ``imageswidthjpg`` will print the first configured ``jpg`` image width to put in a ``width`` element.
 + ``imagessrcjpg`` will print the first configured ``jpg`` image name to put in a ``src`` element.

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

 Simple Lektor Example
----------------

### Lektor Jinja2 Input
```html
<img src="{{ 'waffle.jpg'|imagessrcjpg }}" width="{{ 'waffle.jpg'|imagessrcjpg }}"
  srcset="{{ 'waffle.jpg'|imagessrcsetjpg }}" />
```

### Lektor HTML Output:
```html
<img src="waffle-small.webp" width="512"
  srcset="waffle-small.webp  512w,
          waffle-medium.webp 900w,
          waffle-woowee.webp 1440w," />
```

 Advanced Lektor Example
-------------------------
### Lektor Models Definition
```ini
[fields.my_image]
label = Example Image
description = Select a Image from the Attatchments of this site. Upload one, if no one is available
type = select
source = record.attachments.images
```
### Lektor Jinja2 Input
```html
{% set image = record.attachments.images.get(this.my_image) %}
<img src="{{ image | url | imagessrcwebp }}" width="{{ image | url | imageswidthwebp }}"
     srcset="{{ image | url | imagessrcsetwebp }}" />
```
#### Explaination Input:
- First we created the Jinaja2-variable ``image`` that will contain our image (``this.box_image``) to make this example better readable. *(We assume you know how to create variables in lektor)*
- Next line we created a html image tag with ``src`` and ``width``
- Last we created the ``srcset`` element with all configured sizes.
- By the way we added the [url filter](https://www.getlektor.com/docs/api/templates/filters/url/) in our example. there are options like ``|url(external=true)`` that you could like.

### Lektor HTML Output
```html

<img src="waffle-small.webp" width="512"
  srcset="waffle-small.webp  512w,
          waffle-medium.webp 900w,
          waffle-woowee.webp 1440w," />
```
*(Please note that we added some new lines to make the example better readable ans we assume that ``my_image: waffle.jpg`` comes from your .lr file, created via lektor admin menu)*

 Installation
--------------
```bash
lektor plugin add lektor-image-filter
```
