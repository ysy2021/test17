#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 18:39
# @Author  : ysy
# 模块级别(setup_module/teardown_module)模块始末，全局的，优先级最高
# 函数级别用(setup_function/teardown_function)例生效，函数(不在类中)
# 类级别(setup_class/teardown_class)只在类中前后运行一次，（在类中）
# 方法级(setup_method/teardown_method)开始于方法始末(在类中)
# 类里面(setup/teardown)运用于方法前后
def test_a():
    print('开始测试')


# 函数级别用例生效，函数(不在类中)
def setup_function():
    print('测试前调用')


def teardown_function():
    print("测试后调用")
