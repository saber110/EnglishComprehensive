# -*- coding: utf-8 -*-

class wordsDeal:
    '字处理模块'
    def __init__(self):
        pass

    def sqlEscape(self, old=""):
        '特殊字符转义'
        temp = old.replace("'", "\\'")
        new  =temp.replace('"', '\\"')
        return new

    def getNumber(self, str=""):
        strList = str.split(' ')
        length1 = len(strList)
        length2 = strList.count('')
        return length1 - length2

# a = wordsDeal()
# a.getNumber("JM is a big pig, so what is your ")
# a.sqlEscape("hello , 'aaa'")
