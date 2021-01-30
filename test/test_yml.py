#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 18:39
# @Author  : ysy
import yaml


def test_yaml():
    with open("./dates/calc.yml") as f:
        datas = yaml.safe_load(f)
        # print(datas)
        print(datas['div']['datas'])
