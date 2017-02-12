#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fileinput模块演示

【基本格式】
fileinput.input([files[, inplace[, backup[, bufsize[, mode[, openhook]]]]]])
【默认格式】
fileinput.input (files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)

【参数说明】
files:                  #文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
inplace:                #是否将标准输出的结果写回文件，默认不取代
backup:                 #备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
bufsize:                #缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
mode:                   #读写模式，默认为只读
openhook:               #该钩子用于控制打开的所有文件，比如说编码方式等;

【常用函数】
fileinput.input()       #返回能够用于for循环遍历的对象
fileinput.filename()    #返回当前文件的名称
fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）
fileinput.filelineno()  #返回当前读取的行的行号
fileinput.isfirstline() #检查当前行是否是文件的第一行
fileinput.isstdin()     #判断最后一行是否从stdin中读取
fileinput.close()       #关闭队列

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import sys
import glob
import fileinput

def replace(data, old, new):
    """利用fileinput实现文件内容替换，并将原文件作备份"""
    for line in fileinput.input(data, backup='.bak', inplace=1):
        print(line.rstrip().replace(old, new))

def dos2unix(data):
    """利用fileinput将CRLF文件转为LF"""
    for line in fileinput.input(data, inplace=1):
        if line[-2:] == "\r\n":
            print(line.rstrip() + "\n")
        else:
            print(line.rstrip())

