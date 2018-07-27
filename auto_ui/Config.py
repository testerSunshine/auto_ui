# -*- coding: utf8 -*-
import platform

__author__ = 'MR.wen'
import yaml
import os


def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/config.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s


def get_yaml_local():
    """
    解析本地yaml
    :return:
    """
    if platform.system() == "Windows":
        path = os.path.join('d:\config_auto_ui.yaml')
    else:
        path = os.path.join('/usr/local/autoConfig/config_auto_ui.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s