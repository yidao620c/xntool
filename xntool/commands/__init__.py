#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""

import os
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        if not os.path.exists('/etc/xntool'):
            os.makedirs('/etc/xntool')
        install.run(self)
