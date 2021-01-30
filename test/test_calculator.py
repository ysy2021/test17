#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 18:39
# @Author  : ysy
# 对计算器进行测试
import sys
import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./dates/calc.yml") as f:
        datas = yaml.safe_load(f)
        return datas['add']['datas']


def get_datas2():
    with open("./dates/calc.yml") as f:
        datas = yaml.safe_load(f)
        return datas['div']['datas']


class TestCalc:
    def setup(self):
        print('【开始计算】')

    def teardown(self):
        print('【结束计算】')

    @pytest.mark.parametrize("a,b,result", get_datas())
    def test_add(self, a, b, result):
        calc = Calculator()
        assert result == calc.add(a, b)

    @pytest.mark.parametrize("x,y,result2", get_datas2())
    def test_div(self, x, y, result2):
        calc = Calculator()
        assert result2 == calc.div(x, y)
