#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk
import db

class Add():
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file('ui/addshell.glade')


        self.dialog_add = builder.get_object("dialog_add")

        self.combobox_script = builder.get_object("combobox_script")

        self.entry_addr = builder.get_object("entry_addr")
        self.entry_pass = builder.get_object("entry_pass")
        self.entry_info = builder.get_object("entry_info")

    def run(self):
        resp_id = self.dialog_add.run()
        #print resp_id
        if resp_id == 0:
            self.add_shell()

        self.dialog_add.destroy()

    def add_shell(self):
        addr = self.entry_addr.get_text()
        ps = self.entry_pass.get_text()
        info = self.entry_info.get_text()
        dbconfig = ""
        script = 'php'
        country = 'kr'
        shell = {}
        shell['addr'] = addr
        shell['pass'] = ps
        shell['script'] = script
        shell['country'] = country
        shell['dbconfig'] = dbconfig
        shell['info'] = info
        print shell

        d = db.Db('null.db')
        d.add_a_shell(shell)
        

class Delete():
    pass

class Edit():
    pass

if __name__ == '__main__':
    dialog = Add()
    dialog.run()
