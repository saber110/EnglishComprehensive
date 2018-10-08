# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib, re
import mysql
from bs4 import BeautifulSoup
import config

class Spider:
    'It is performed by every category'
    def __init__(self, url, table):
        """url is the goal url
        table is the database table for this url
        get category`s list
        """
        self.url = url
        self.table = table
        self.domain = config.domain

    def Getlist(self):
        result = []
        page = urllib.urlopen(self.url)
        soup = BeautifulSoup(page, "html.parser")
        list = soup.find(id="content-listing")
        ul = list.ul
        for item in ul.find_all('li',recursive=False):
            href = item.a['href']
            summary = item.find(class_="story_link")
            title   = summary.contents
            temp    = {'href' : self.domain + href, "title" : title[0].strip() }
            result.append(temp)
        return result

    def hrefFor2018(self):
        """
        the artical`s href published in 2018
        """
        result = []
        for item in self.Getlist():
            if str(config.goalYear) in item['href']:
                result.append(item)
        return result

    def contentOfArtical(self, href):
        """
        get the contents of linked by the href
        """
        result = []
        page = urllib.urlopen(href)
        soup = BeautifulSoup(page, "html.parser")
        # temp = soup.find(class_="small-centered small-12 columns")
        title = soup.find(id="headline").get_text()
        title = title.strip().encode("utf8")
        temp = soup.find(class_=re.compile("story-two eza-body*"))
        content = temp.find_all('p',recursive=False)
        for item in content:
            result.append(item.encode("utf8"))
        contents = ''.join(result)
        dict = {'title':title,'content':contents}
        return dict

# spider1 = Spider("http://127.0.0.1/Lists.html", "test")
# print spider1.contentOfArtical("http://127.0.0.1/test1.html")
# spider1.Getlist();
