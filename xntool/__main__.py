#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main func

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
from xntool.tail import main as main02
from xntool.gexcel import main as main03
from xntool.gjavabean import main as main04
from xntool.love import main as main05
from xntool.xqiniu import main as main06
from xntool.xfileinput import dos2unix, replace
from xntool.md5 import md5sum
import sys
from sys import stderr as e

def _main(args):
    """主函数入口"""
    if len(args) < 2:
        e.write('wrong arguments, exit\n')
        exit(1)
    elif args[1] == 'tail':
        if len(args) != 4:
            e.write('Usage: xntool tail /var/log/web.log python\n')
            exit(1)
        main02(args[2], args[3])
    elif args[1] == 'gexcel':
        if len(args) != 4:
            e.write('Usage: xntool gexcel /tmp/schema.excel /tmp/schema.sql\n')
            exit(1)
        main03(args[2], args[3])
    elif args[1] == 'gjavabean':
        if len(args) != 5:
            e.write('Usage: xntool gjavabean /tmp/pkg/ pkg; /tmp/schema.sql\n')
            exit(1)
        main04(args[2], args[3], args[4])
    elif args[1] == 'love':
        main05()
    elif args[1] == 'qiniu':
        if len(args) != 3:
            e.write('Usage: xntool qiniu /tmp/pics\n')
            exit(1)
        main06(args[2])
    elif args[1] == 'dos2unix':
        if len(args) != 3:
            e.write('Usage: xntool dos2unix data.txt\n')
            exit(1)
        dos2unix(args[2])
    elif args[1] == 'replace':
        if len(args) != 5:
            e.write('Usage: xntool replace data.txt python perl\n')
            exit(1)
        replace(args[2], args[3], args[4])
    elif args[1] == 'md5':
        if len(args) != 3:
            e.write('Usage: xntool md5 data.txt\n')
            exit(1)
        md5sum(args[2])
    else:
        e.write('wrong arguments, exit\n')
        exit(1)

def main():
    _main(sys.argv)

