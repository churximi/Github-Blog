#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：更新github博客
时间：2018年04月22日19:32:04
"""
import os


def update_blog():
    os.chdir("/Users/simon/hexo")
    os.system("hexo g")
    os.system("hexo d")


if __name__ == "__main__":
    update_blog()
