
import mysql, config
import urllib
from bs4 import BeautifulSoup
from Spider import Spider
from wordsDeal import wordsDeal
from myEmail import email
def going(url):
    text = wordsDeal()
    spider1 = Spider(url, 'test')
    hrefs = spider1.hrefFor2018()
    for item in hrefs:
        try:
            content = str(spider1.contentOfArtical(item['href']))
            wordNum = text.getNumber(content)
            if wordNum > config.minimum and wordNum < config.maximum:
                query = "insert into Christian(href,title, content, wordNum) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(item['title']) + "','" + text.sqlEscape(content) + "','" + str(wordNum) + "');"
                sqlQuery(query)
                mail.sendAuto(text.sqlEscape(content))
        except BaseException as error:
            query = "insert into SpiderExcept(href,except) values ( '" + text.sqlEscape(item['href']) + "','" + text.sqlEscape(str(error)) +"');"
            sqlQuery(query)
        else:		
            print wordNum," | ",item['title']
    del spider1

def sqlQuery(sql = ""):
    db = mysql.connect()
    mysql.query(db,sql)
    mysql.close(db)

def main():
    mail = email()
    for item in config.category:
        try:
            going(item)
        except BaseException as error:
            print error

main()
