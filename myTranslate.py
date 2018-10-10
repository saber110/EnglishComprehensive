#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate

def TransToChinese(str):
    return translate(str, 'zh-CN')

# if __name__ == '__main__':
#     main()
