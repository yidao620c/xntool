#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2017 Xiong Neng
#
# Licensed under the MIT License;
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages
from xntool.commands import CustomInstallCommand
import xntool

setup(
    name='xntool',
    version=xntool.__version__,
    description='funny tools',
    long_description=open("README.rst").read(),
    url='https://github.com/yidao620c/xntool',
    author='Xiong Neng',
    author_email='yidao620@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords=['xntool', 'qiuniu', 'excel', 'pdf', 'mysql'],
    packages=find_packages(),
    # Project uses , so ensure
    install_requires=[
        "qiniu>=7.1.1",
        "lxml>=3.7.2",
        "openpyxl>=2.4.2",
        "requests>=2.6.0",
    ],
    # building source ”python setup.py sdist“ use MANIFEST.in
    # building binary ”python setup.py bdist“ use package_data
    package_data={
        # If any package contains *.txt or *.md files, include them:
        '': ['*.txt', '*.md', '*.rst', '*.in'],
        # include any *.conf files found in the 'etc' package, too:
        'etc': ['*.conf'],
    },
    # The data_files option can be used to specify additional files
    # needed by the module distribution: configuration files,
    # message catalogs, data files
    data_files=[('etc/xntool', ['etc/xntool.conf']), ],
    cmdclass={'install': CustomInstallCommand},
    entry_points={
        # "xntool.registered_commands": [
        #     "upload = xntool.commands.upload:main",
        #     "register = xntool.commands.register:main",
        # ],
        "console_scripts": [
            "xntool = xntool.__main__:main",
        ],
    },
)
