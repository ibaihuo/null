#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk

class Manager():
    def __init__(self):
        cmd_textview = gtk.TextView()
        
        cmd_scrolle = gtk.ScrolledWindow()
        db_scrolle = gtk.ScrolledWindow()
        file_scrolle = gtk.ScrolledWindow()
        cmd_scrolle.add(cmd_textview)

        cmd_entry = gtk.Entry()
        cmd_entry.set_size_request(400, 75)
        run_button = gtk.Button("Run")
        run_button.set_size_request(100, 75)
        clear_button = gtk.Button("Clear")
        clear_button.set_size_request(100, 75)        

        run_hbox = gtk.HBox(3)
        run_hbox.pack_start(cmd_entry)
        run_hbox.pack_start(run_button, expand=False, fill=False)
        run_hbox.pack_start(clear_button, expand=False, fill=False)

        cmd_status = gtk.Statusbar()
        
        cmd_vbox = gtk.VBox(3)
        cmd_vbox.pack_start(cmd_scrolle)
        cmd_vbox.pack_start(run_hbox, expand=False, fill=False)
        cmd_vbox.pack_start(cmd_status, expand=False, fill=False)

        db_vbox = gtk.VBox(2)
        db_vbox.pack_start(db_scrolle)


        file_vbox = gtk.VBox(2)
        file_vbox.pack_start(file_scrolle)


        cmd_label = gtk.Label("Terminal")
        db_label = gtk.Label("Database")
        file_label = gtk.Label("Filemanager")

        note = gtk.Notebook()
        note.append_page(cmd_vbox, cmd_label)
        note.append_page(db_vbox, db_label)
        note.append_page(file_vbox, file_label)

        ip_label = gtk.Label("IP 123.123.123.123")

        self.vbox = gtk.VBox(2)
        self.vbox.pack_start(ip_label, True, True,0)
        self.vbox.pack_start(note, True, True, 0)

        self.vbox.show_all()

        #print self.vbox.query_child_packing(ip_label)

        # #print notebook.get_current_page()
        # if notebook.get_current_page() == 0:
        #     self.terminal.init_terminal('http://127.0.0.1/null/shell.php')
        # elif notebook.get_current_page() == 1:
        #     self.filemanager.init_filemanager()


if __name__ == '__main__':
    win = gtk.Window()
    win.show()
    win.connect("destroy",gtk.main_quit)
    one = Manager()

    win.add(one.vbox)
    gtk.main()
