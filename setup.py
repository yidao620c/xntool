#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='xntool',
    version='0.2.4',
    packages=find_packages(),
    # Project uses , so ensure
    install_requires=[
        "qiniu>=7.1.1",
        "lxml>=3.7.2",
        "openpyxl>=2.4.2",
        "requests>=2.6.0",
    ],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # include any *.msg files found in the 'test' package, too:
        'test': ['*.msg'],
    },
    description='funny tools',
    url='https://github.com/yidao620c/xntool',
    author='Xiong Neng',
    author_email='yidao620@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['xntool', 'qiuniu', 'excel', 'pdf', 'mysql'],
    entry_points={
        # "xntool.registered_commands": [
        #     "upload = twine.commands.upload:main",
        #     "register = twine.commands.register:main",
        # ],
        "console_scripts": [
            "xntool = xntool.__main__:main",
        ],
    },
)

