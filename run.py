
import mysql, config
import urllib
from bs4 import BeautifulSoup
from Spider import Spider

def going():
    spider1 = Spider('https://www.csmonitor.com/World/(view)/all', 'test')
    hrefs = spider1.hrefFor2018()
    for item in hrefs:
        content = str(spider1.contentOfArtical(item['href']))
        query = "insert into Christian(href,title, content) values ( '" + item['href'] + "','" + item['title'] + "','" + content + ");"
        sqlQuery(query)


def sqlQuery(sql = ""):
    db = mysql.connect()
    mysql.query(db,sql)
    mysql.close(db)

# sqlQuery("select * from Christian");
going()
