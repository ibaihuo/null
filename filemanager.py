#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk
import os.path

import filepost

class Filemanager():
    """yun
    """
    def __init__(self, builder):
        """
        Arguments:
        - `builder`:
        """
        self.builder = builder

        self.folder_pix = gtk.gdk.pixbuf_new_from_file('folder.svg')

        self.treeview_dir = self.builder.get_object("treeview_dir")
        self.treeview_file = self.builder.get_object("treeview_file")

        self.statusbar_file = self.builder.get_object("statusbar_file")

        self.set_dir_header_title()
        self.set_filelist_title()

        self.entry_path = self.builder.get_object("entry_path")
        self.entry_path.connect("activate",self.get_path_singal)

        self.button_path = self.builder.get_object("button_path")
        self.button_path.connect("clicked", self.get_path_singal)

        self.treestore_dir = self.builder.get_object("treestore_dir")
        self.liststore_file = self.builder.get_object("liststore_file")

        self.treeview_file.connect("row-activated", self.open_dir)

    def init_filemanager(self):
        self.current_path = filepost.init_filemanager('http://127.0.0.1/null/shell.php')
        #print 'current:', self.current_path
        self.entry_path.set_text(self.current_path)
        res_dirs, res_files = self.get_path_content()

        #print res_dirs, res_files
        self.display_dirs(res_dirs)
        self.display_files(res_dirs + res_files)        

    def display_dirs(self, res_dirs):
        #print self.current_path
        dirs = self.current_path.split('/')[1:]
        #print dirs
        self.treestore_dir.clear()
                
        mypiter = self.treestore_dir.append(None)
        self.treestore_dir.set(mypiter,
                               0, self.folder_pix,
                               1, "/",
                               )

        last_iter = self.__create_dir_tree(mypiter,dirs)
        self.create_current_dirs(last_iter, res_dirs)

        self.treeview_dir.expand_all()


    def get_path_content(self):
        return filepost.get_path("http://127.0.0.1/null/shell.php", self.current_path)


    def get_path_singal(self,widget):
        self.current_path  = self.entry_path.get_text()
        if not self.current_path.endswith('/'):
            self.current_path += '/'

        self.entry_path.set_text(self.current_path)
        res_dirs, res_files = self.get_path_content()
        #print res_dirs, res_files
        
        self.display_files(res_dirs + res_files)
        
    def display_files(self,res):
        """
        """
        self.liststore_file.clear()     # 清除原有数据

        for i in res:
            li_iter = self.liststore_file.append()
            self.liststore_file.set(li_iter,
                                     0, i[0],
                                     1, i[1],
                                     2, i[2],
                                     3, i[3],
                                     )

    def open_dir(self, treeview, path, view_column):
        #print treeview,path,view_column
        iter = self.liststore_file.get_iter(path)
        dir = self.liststore_file.get_value(iter, 0)
        #print dir
        dir = dir.strip()
        if dir.endswith('/'):
            #print dir
            if '..' == dir[:2]:
                if self.current_path == '/':
                    pass
                else:
                    self.current_path ='/'.join(self.current_path.split('/')[:-2]) + '/'
            elif '.' == dir[:1]:
                pass
            else:
                self.current_path = os.path.join(self.current_path,dir)
            self.entry_path.set_text(self.current_path)
            #self.entry_path.activated()

            res_dirs, res_files = self.get_path_content()
            self.display_dirs(res_dirs)
            self.display_files(res_dirs + res_files)

    def __create_dir_tree(self, piter, dirs):
        d = dirs[0]

        child_iter = self.treestore_dir.append(piter)
        self.treestore_dir.set(child_iter,
                               0, self.folder_pix,
                               1, d)

        if len(dirs) > 1:
            self.__create_dir_tree(child_iter, dirs[1:])

        return child_iter

    def create_current_dirs(self, iter, res_dirs):
        for d in res_dirs:
            child_iter = self.treestore_dir.append(iter)
            #print d
            self.treestore_dir.set(child_iter,
                                   0, self.folder_pix,
                                   1, d[0][:-1])

    def set_dir_header_title(self):
        # head_title = gtk.TreeViewColumn("PIX", gtk.CellRendererPixbuf())
        # self.treeview_dir.append_column(head_title)
        head_title = gtk.TreeViewColumn("DIRS", gtk.CellRendererText(), text = 1)
        self.treeview_dir.append_column(head_title)
        


    def set_filelist_title(self):
        """设置标题行
        """
        head_title = gtk.TreeViewColumn("Name", gtk.CellRendererText(), text = 0)
        head_title.set_sort_column_id(0)
        self.treeview_file.append_column(head_title)

        head_title = gtk.TreeViewColumn("Date", gtk.CellRendererText(), text = 1)
        self.treeview_file.append_column(head_title)

        head_title = gtk.TreeViewColumn("Size", gtk.CellRendererText(), text = 2)
        self.treeview_file.append_column(head_title)

        head_title = gtk.TreeViewColumn("Permission", gtk.CellRendererText(), text = 3)
        self.treeview_file.append_column(head_title)


if __name__ == '__main__':
    builder = gtk.Builder()
    builder.add_from_file('ui/null.glade')
    win_main = builder.get_object("window_main")
    win_main.connect("destroy",gtk.main_quit)

    f = Filemanager(builder)
    f.init_filemanager()
    
    gtk.main()
