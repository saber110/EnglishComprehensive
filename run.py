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
            if content['content'] != "contents":
                query = "insert into Christian(href,title, content, sent) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(item['title']) + "','" + text.sqlEscape(content['content']) + "','" + config.notSend +"');"
                sqlQuery(query)
                print "YES ", item['title']
                # mail.sendAuto(content['title'], content['content'] + '<p>' + Chinese + '</p>')
        except BaseException as error:
            query = "insert into SpiderExcept(href,except) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(str(error)) +"');"
            sqlQuery(query)
        else:
            print "NO ", item['title']
    del spider1
    del text
    del mail

def sqlQuery(sql = ""):
    db = mysql.connect()
    mysql.query(db,sql)
    mysql.close(db)

def main():
    offset = 920
    category = ["https://www.csmonitor.com/USA/(offset)/"+str(offset)+"/(view)/all", \
"https://www.csmonitor.com/World/(offset)/"+str(offset)+"/(view)/all", \
"https://www.csmonitor.com/Commentary/(offset)/"+str(offset/2)+"/(view)/all", \
"https://www.csmonitor.com/Science/(offset)/"+str(offset/20)+"/(view)/all", \
"https://www.csmonitor.com/Business/(offset)/"+str(offset/7)+"/(view)/all", \
"https://www.csmonitor.com/Environment/(offset)/"+str(offset/6)+"/(view)/all", \
"https://www.csmonitor.com/Technology/(offset)/"+str(offset/11)+"/(view)/all", \
"https://www.csmonitor.com/The-Culture/(offset)/"+str(offset/3)+"/(view)/all", \
"https://www.csmonitor.com/Books/(offset)/"+str(offset/4)+"/(view)/all"]
    while offset >= 20:
        #print "offset", offset
        #a = raw_input("input")
        for item in category:
            try:
                going(item)
            except BaseException as error:
                print error
        offset = offset - 20
        category = ["https://www.csmonitor.com/USA/(offset)/"+str(offset)+"/(view)/all", \
"https://www.csmonitor.com/World/(offset)/"+str(offset)+"/(view)/all", \
"https://www.csmonitor.com/Commentary/(offset)/"+str(offset/2)+"/(view)/all", \
"https://www.csmonitor.com/Science/(offset)/"+str(offset/20)+"/(view)/all", \
"https://www.csmonitor.com/Business/(offset)/"+str(offset/7)+"/(view)/all", \
"https://www.csmonitor.com/Environment/(offset)/"+str(offset/6)+"/(view)/all", \
"https://www.csmonitor.com/Technology/(offset)/"+str(offset/11)+"/(view)/all", \
"https://www.csmonitor.com/The-Culture/(offset)/"+str(offset/3)+"/(view)/all", \
"https://www.csmonitor.com/Books/(offset)/"+str(offset/4)+"/(view)/all"]

main()
