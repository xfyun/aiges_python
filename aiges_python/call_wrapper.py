#!/usr/bin/env python
# coding:utf-8
""" 
@author: nivic ybyang7
@license: Apache Licence 
@file: call_wrapper.py
@time: 2022/06/15
@contact: ybyang7@iflytek.com
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import errno
import inspect
import argparse
import importlib
from logging import exception
from msilib.schema import Error
import re
import string
from tkinter import W



def call_wrapper(args):
    print(args)

    # 类型检查
    mod = importlib.import_module("wrapper")
 
    CheckFunc_Run(mod,"wrapperInit",['int', 'int'])
    CheckFunc_Run(mod,"wrapperOnceExec",['str', 'dict', 'list', 'list', 'list', 'int'])
    CheckFunc_Run(mod,"wrapperDestroy",['str'])

    mod.wrapperInit(1,2)
    mod.wrapperOnceExec("www",{"w":1234},[1,2],[1,2],[1,2],5)
    mod.wrapperDestroy("destory")
    
    print(dir(mod))
    print("call done")


def CheckFunc_Run(mod,func_name,func_parameter_list):
    if "wrapperOnceExec" in dir(mod): #判断文件是否存在
        print("nice ...")
    wrapperOnceExec =getattr(mod, "wrapperOnceExec")
    paramter_num = wrapperOnceExec.__code__.co_argcount 
    if paramter_num == 2:# 判断函数参数个数
        print("nice ...")
    ins,outs = str(inspect.signature(wrapperOnceExec)).split("->")
    ins_list = re.sub('\(|\)', '', ins).replace(' ', '').split(",")
    cate_list = []
    for i in range(len(func_parameter_list)):
        _ , cate = ins_list[i].split(":")
        tl_cate = func_parameter_list[i]
        if tl_cate != cate:
            print("The parameter type match error...")
    print("The parameter type match was successful...")



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=str,
                        default='wrapper.py',
                        help='wrapper.py file location')

    args = parser.parse_args()

    call_wrapper(args.w)

if __name__ == '__main__':
    main()