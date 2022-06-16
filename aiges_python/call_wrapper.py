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
import inspect
import argparse
import importlib
from logging import exception
from PIL import Image
import logging
import re

logging.getLogger().setLevel(logging.INFO)  # 设置log等级


def call_wrapper(args):
    print(args)

    img_PIL = Image.open("aiges_python\yeye.jpg")
    reqData = [{"data":img_PIL}]
    

    # 类型检查
    mod = importlib.import_module("wrapper_copy")

    CheckFunc_Run(mod, "wrapperInit", ['dict'])
    CheckFunc_Run(mod, "wrapperOnceExec", [
                  'str', 'dict', 'list', 'list', 'list', 'int'])
    CheckFunc_Run(mod, "wrapperDestroy", ['str'])

    mod.wrapperInit({"he": "ha"})
    mod.wrapperOnceExec("www", {"w": 1234}, reqData, [1, 2], [1, 2], 5)
    mod.wrapperDestroy("destory")

    logging.info("Wraper function has been checked and ran successfully ")


def CheckFunc_Run(mod, func_name, func_parameter_list):
    if func_name in dir(mod):  # 判断文件是否存在
        print("nice ...")
    wrapperOnceExec = getattr(mod, func_name)
    paramter_num = wrapperOnceExec.__code__.co_argcount
    if paramter_num == len(func_parameter_list):  # 判断函数参数个数
        print("nice ...")
    ins, outs = str(inspect.signature(wrapperOnceExec)).split("->")
    ins_list = re.sub('\(|\)', '', ins).replace(' ', '').split(",")
    cate_list = []
    for i in range(len(func_parameter_list)):
        _, cate = ins_list[i].split(":")
        tl_cate = func_parameter_list[i]
        if tl_cate != cate:
            logging.error("The parameter type match error...")
    logging.info("The parameter type match was successful...")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=str,
                        default='wrapper.py',
                        help='wrapper.py file location')

    args = parser.parse_args()

    call_wrapper(args.w)


if __name__ == '__main__':
    main()
