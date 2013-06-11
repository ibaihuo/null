#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk

xxoo = gtk.Builder()
xxoo.add_from_file('../ui/site.glade')
vbox_site = xxoo.get_object("vbox_site")
#vbox_site = gtk.VBox(3)
lb = gtk.Label(site)
#print vbox_db
#self.notebook.append_page(vbox_site, lb)
