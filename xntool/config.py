#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""

import codecs
import platform

_pyverstion = platform.python_version()
if _pyverstion.startswith('2'):
    import ConfigParser as configparser
else:
    import configparser

_cfgfile = "/etc/xntool/xntool.conf"
_config = configparser.ConfigParser(allow_no_value=True)
with codecs.open(_cfgfile, "r", "utf-8-sig") as f:
    _config.read_file(f)


def cfg(section, key):
    return _config.get(section, key)
