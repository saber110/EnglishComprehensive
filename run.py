
import mysql, config
import urllib
from bs4 import BeautifulSoup
from Spider import Spider
from wordsDeal import wordsDeal
def going(url):
    text = wordsDeal()
    spider1 = Spider(url, 'test')
    hrefs = spider1.hrefFor2018()
    for item in hrefs:
        content = str(spider1.contentOfArtical(item['href']))
        wordNum = text.getNumber(content)
        if wordNum > config.minimum and wordNum < config.maximum:
            query = "insert into Christian(href,title, content) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(item['title']) + "','" + text.sqlEscape(content) + "');"
            sqlQuery(query)
	    print item['title'], "|" , wordNum
    del spider1

def sqlQuery(sql = ""):
    db = mysql.connect()
    mysql.query(db,sql)
    mysql.close(db)

def main():
    for item in config.category:
        going(item)

main()
