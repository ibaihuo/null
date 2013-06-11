#!/usr/bin/env python
#-*- coding:utf-8 -*-

import codecs
#import wordpath
import sqlite3

class Db():
    """连接数据库
    """
    def __init__(self, database):
        """

        Arguments:
        - `database`:数据库相应路径
        """
        self._database = database
        self.__connect()

    def __connect(self):
        """连接数据库函数
        
        Arguments:
        - `self`:
        """
        self.conn = sqlite3.connect(self._database)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_all_shells(self):
        """获得单词
        """
        self.cursor.execute(
            """
            SELECT * FROM  shell order by id
            """)
        #print self.cursor.fetchone()

        shell_list = []

        for row in self.cursor:
            shell = {}
            #print row
            shell['addr'] = row['addr']
            shell['pass'] = row['pass']
            shell['script'] = row['script']
            shell['country'] = row['country']
            shell['dbconfig'] = row['dbconfig']
            shell['info'] = row['info']
            shell_list.append(shell)

        return shell_list

    def add_a_shell(self, shell):
        """
        """
        self.cursor.execute("INSERT INTO shell values(NULL, ?, ?, ?, ?, ?, ?)",
                                     (shell['addr'],
                                      shell['pass'],
                                      shell['script'],
                                      shell['country'],
                                      shell['dbconfig'],
                                      shell['info']))

        self.conn.commit()

    def create_new_table(self, table):
        """创建新数据表
        """
        self.cursor.execute(
            """
            CREATE TABLE %s (
            id integer PRIMARY KEY,
            addr varchar(200) NOT NULL,
            pass varchar(20) NOT NULL, 
            script varchar(200) NOT NULL,
            country varchar(200), 
            dbconfig varchar(100),
            info varchar(200))
            """ % table)


if __name__ == '__main__':
    db = Db('null.db')
    #db.create_new_table('shell')
    print db.get_all_shells()
