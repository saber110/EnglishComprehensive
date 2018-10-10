# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import mysql, config
import urllib
from bs4 import BeautifulSoup
from Spider import Spider
from wordsDeal import wordsDeal
from myEmail import email
def going(url):
    mail = email()
    text = wordsDeal()
    spider1 = Spider(url, 'test')
    hrefs = spider1.hrefFor2018()
    for item in hrefs:
        try:
            content = spider1.contentOfArtical(item['href'])
            if content != False:
                query = "insert into Christian(href,title, content, sent) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(item['title']) + "','" + text.sqlEscape(content['content']) + "','" + config.notSend +"');"
                sqlQuery(query)
                # mail.sendAuto(content['title'], content['content'] + '<p>' + Chinese + '</p>')
        except BaseException as error:
            query = "insert into SpiderExcept(href,except) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(str(error)) +"');"
            sqlQuery(query)
        else:
            print item['title']
    del spider1
    del text
    del mail

def sqlQuery(sql = ""):
    db = mysql.connect()
    mysql.query(db,sql)
    mysql.close(db)

def main():
    for item in config.category:
        try:
            going(item)
        except BaseException as error:
            print error

main()
