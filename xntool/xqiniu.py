#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 七牛上传图片并
Desc : 
"""

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os
from os.path import join
import sys
from xntool.config import cfg

# 需要填写你的 Access Key 和 Secret Key
ACCESS_KEY = cfg('qiniu', 'ACCESS_KEY')
SECRET_KEY = cfg('qiniu', 'SECRET_KEY')
# 七牛空间URL
URL_PRE = cfg('qiniu', 'URL_PRE')
# 要上传的空间名
BUCKET_NAME = cfg('qiniu', 'BUCKET_NAME')


def main(pic_dir):
    # 构建鉴权对象
    q = Auth(ACCESS_KEY, SECRET_KEY)
    pfs = [f for f in os.listdir(pic_dir)
           if os.path.isfile(join(pic_dir, f))
           and not f.endswith('url.txt') and not f.endswith('.py')]
    urls = []
    for f in pfs:
        localfile = join(pic_dir, f)
        if os.path.isfile(localfile) and f != 'url.txt':
            # 上传到七牛后保存的文件名
            key = f
            # 生成上传 Token，可以指定过期时间等
            token = q.upload_token(BUCKET_NAME, key, 3600)
            # 要上传文件的本地路径
            ret, info = put_file(token, key, localfile)
            # 上传完后删除文件
            os.remove(localfile)
            # 将url写入文本
            urls += URL_PRE + f + '\n'

    with open(os.path.join(pic_dir, 'url.txt'), 'a', encoding='utf-8') as uf:
        uf.writelines(urls)
