#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""

import os
import sys
import shutil
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        # move configuration directory
        # print('CustomInstallCommand.. {}'.format(os.path.join(sys.prefix, 'etc/xntool')))
        # try:
        #     shutil.move(os.path.join(sys.prefix, 'etc/xntool'), '/etc/')
        # except:
        #     pass

