
import mysql, config
import urllib
from bs4 import BeautifulSoup
from Spider import Spider

def going():
    spider1 = Spider('https://www.csmonitor.com/World/(view)/all', 'test')
    hrefs = spider1.hrefFor2018()
    for item in hrefs:
        content = str(spider1.contentOfArtical(item['href']))
        query = "insert into Christian(href,title, content) values ( '" + sqlEscape(item['href']) + "','" + sqlEscape(item['title']) + "','" + sqlEscape(content) + "');"
        sqlQuery(query)
	print item['title']


def sqlQuery(sql = ""):
    db = mysql.connect()
    mysql.query(db,sql)
    mysql.close(db)

def sqlEscape(old = ""):
    temp = old.replace("'", "\\'")
    new  =temp.replace('"', '\\"')
    return new

# sqlQuery("select * from Christian");
going()
