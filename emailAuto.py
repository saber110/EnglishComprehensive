# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import config, mysql
from myEmail import email

class emailAuto(object):
    """docstring for emailAutoself.
    按数据库每天自动执行推送相应消息"""
    def __init__(self, arg=""):
        super(emailAuto, self).__init__()
        self.arg = arg

    def SqlInstruct(self, limit = 0, id = 0,func = "select"):
        if func == "select":
            sql = "select id, title, content from Christian where sent = '"+ config.notSend +"' limit " + str(limit)
        else:
            sql = "update Christian set sent = '" + config.send + "' where id = " + str(id)
        return sql

    def getMysql(self, sql):
        db = mysql.connect()
        result = mysql.getData(db, sql)
        mysql.close(db)
        return result

    def queryMysql(self, sql):
        db = mysql.connect()
        mysql.query(db, sql)
        mysql.close(db)

    def test(self):
        mail = email()
        set = self.getMysql(self.SqlInstruct(config.reIncreament))
        for item in set:
            mail.sendAuto(item['title'], item['content'])
            self.queryMysql(self.SqlInstruct(id = item['id'], func = "update"))

test1 = emailAuto()
test1.test()
