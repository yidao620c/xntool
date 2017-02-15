#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小熊工具箱

每天一句情话 撩女朋友专用：
xntool love

tail查看关键字：
xntool tail /var/log/web.log 'python'


将windows换行符转换成unix换行符：
xntool dos2unix /var/log/web.log

内容替换：
xntool replace data.txt python perl

文件的md5值：
xntool md5 data.txt

七牛存储图片上传：
首先进入你的七牛主页，拿到必要配置参数，修改配置文件`/usr/etc/xntool/xntool.conf`中的[qiniu]部分：
[qiniu]
# Access Key
ACCESS_KEY=xxxxxxxxxxxxxxxx
# Secret Key
SECRET_KEY=yyyyyyyyyyyyyy
# 七牛空间URL
URL_PRE=http://yidaospace.qiniudn.com/
# 要上传的空间名
BUCKET_NAME=yidaospace

使用：
xntool qiniu /tmp/pics

上传完后会自动删除图片并且将url写入图片目录下的url.txt最后

mysql schema转换为excel:
xntool gexcel /tmp/schema.excel /tmp/schema.sql
其中schema.sql文件格式示例：
-- -----------------------贷快发二期数据库-------------------------------
-- 公共用户表
DROP TABLE IF EXISTS t_public_user;
CREATE TABLE t_public_user (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  user_type         INTEGER COMMENT '用户类型 1:企业用户 2:个人用户',
  account           VARCHAR(20) NOT NULL COMMENT '账号',
  password          VARCHAR(32) NOT NULL COMMENT '密码',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '公共用户表';

-- 贷款申请表
DROP TABLE IF EXISTS t_apply;
CREATE TABLE t_apply (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '贷款申请表';

mysql schema转换为javabean：
xntool gjavabean /tmp/pkg/ pkg; /tmp/schema.sql
其中schema.sql文件格式示例同上

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
import xntool
import sys
from sys import stderr as e

def _main(args):
    """主函数入口"""
    if len(args) < 2:
        e.write('wrong arguments, exit\n')
        exit(1)
    elif args[1] == '--help':
        print(__doc__)
    elif args[1] == '--version':
        print(xntool.__version__)
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

