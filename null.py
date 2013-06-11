#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk
import os.path

import manager
import db

# import shell
# import terminal
# import filemanager

class Null():
    """NULL
    """
    def __init__(self, builder):
        """
        Arguments:
        - `builder`:
        """
        self.builder = builder

        self.liststore_shell = self.builder.get_object("liststore_shell")

        self.treeview_shell = self.builder.get_object("treeview_shell")
        self.treeview_shell.connect("row-activated", self.shell_choose)

        self.textview_res = self.builder.get_object("textview_res")

        self.notebook = self.builder.get_object("notebook")

        self.statusbar_shell = self.builder.get_object("statusbar_shell")

        # self.notebook.connect("switch-page", self.switch_page)

        self.set_shell_title()

        self.create_shell_list()



        # self.terminal = terminal.Terminal(self.builder)
        # self.filemanager = filemanager.Filemanager(self.builder)

        menu = gtk.Menu()
        #Fill it with menu items

        item_terminal = gtk.MenuItem("Terminal")
        item_file = gtk.MenuItem("File Manager")
        item_db = gtk.MenuItem("DataBase")
        item_refresh = gtk.MenuItem("Refresh")
        item_new = gtk.MenuItem("New")
        item_del = gtk.MenuItem("Del")
        item_sep = gtk.SeparatorMenuItem()
        item_sep2 = gtk.SeparatorMenuItem()
        item_edit = gtk.MenuItem("Edit")
        
        menu.append(item_terminal)
        menu.append(item_file)
        menu.append(item_db)
        menu.append(item_sep)
        menu.append(item_refresh)
        menu.append(item_sep2)
        menu.append(item_new)
        menu.append(item_edit)
        menu.append(item_del)
        
        item_terminal.show()
        item_file.show()
        item_db.show()
        item_sep.show()
        item_sep2.show()
        item_refresh.show()
        item_new.show()
        item_edit.show()
        item_del.show()

        item_new.connect("activate", self.run_add_dialog)
        
        self.treeview_shell.connect_object("event", self.right_button_press, menu)

    def right_button_press(self, widget, event):
        if event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
            #make widget popup
            widget.popup(None, None, None, event.button, event.time)
            pass

    def set_shell_title(self):
        """设置标题行
        """
        head_title = gtk.TreeViewColumn("ID", gtk.CellRendererText(), text = 0)
        head_title.set_sort_column_id(0)
        self.treeview_shell.append_column(head_title)

        head_title = gtk.TreeViewColumn("SCRIPT", gtk.CellRendererText(), text = 1)
        self.treeview_shell.append_column(head_title)

        head_title = gtk.TreeViewColumn("COUNTRY", gtk.CellRendererText(), text = 2)
        self.treeview_shell.append_column(head_title)

        head_title = gtk.TreeViewColumn("SHELL", gtk.CellRendererText(), text = 3)
        self.treeview_shell.append_column(head_title)

        head_title = gtk.TreeViewColumn("PASS", gtk.CellRendererText(), text = 4)
        self.treeview_shell.append_column(head_title)

        head_title = gtk.TreeViewColumn("INFO", gtk.CellRendererText(), text = 5)
        self.treeview_shell.append_column(head_title)

    def run_add_dialog(self,widget):
        dialog = shell.Add()
        dialog.run()
        self.create_shell_list()

    # def switch_page(self, notebook, move_focus, test):

    def shell_choose(self, treeview, path, view_column):
        (model, iter) = treeview.get_selection().get_selected()
        url = model.get_value(iter, 3)
        script = model.get_value(iter, 2)
        p = model.get_value(iter,4)
        host = url[7:].split('/')[0]
        print url,p,script


        m = manager.Manager()
        l = gtk.Label(host)
        self.notebook.append_page(m.vbox, l)

        # self.notebook.set_current_page(1)
        
       
    def create_shell_list(self):
        """
        """
        self.liststore_shell.clear()     # 清除原有数据

        shell = db.Db('null.db')
        shell_list = shell.get_all_shells()
        slen = len(shell_list)

        #print self.shell_list, len(self.shell_list)
        for s in range(slen):
            li_iter = self.liststore_shell.append()
            self.liststore_shell.set(li_iter,
                                     0, s+1,
                                     1, shell_list[s]['country'],
                                     2, shell_list[s]['script'],
                                     3, shell_list[s]['addr'],
                                     4, shell_list[s]['pass'],
                                     5, shell_list[s]['info'],
                                     )

        self.statusbar_shell.push(1,"Your have %s Shells." % slen)

if __name__ == '__main__':
    builder = gtk.Builder()
    builder.add_from_file('ui/main.glade')
    win_main = builder.get_object("window_main")
    win_main.connect("destroy",gtk.main_quit)

    Null(builder)
    
    gtk.main()
