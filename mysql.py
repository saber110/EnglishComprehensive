#!/usr/bin/env python
# coding=utf-8
import MySQLdb
import config
import MySQLdb.cursors

def connect():
    db=MySQLdb.connect(config.host, config.username, config.password, config.database, charset='utf8',cursorclass=MySQLdb.cursors.DictCursor)
    return db

def getData(db, query, table):
    c=db.cursor()
    c.execute(query)
    data = c.fetchall()
    c.close()
    return data

def query(db,query):
    c=db.cursor()
    c.execute(query)
    db.commit()
    c.close()

def close(db):
    db.close()

