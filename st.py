#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk

class Manager():
    def __init__(self):
        self.vbox = gtk.VBox(3)

        ip_label = gtk.Label("IP 123.123.123.123")

        self.vbox.pack_start(ip_label)
        self.vbox.show()
        ip_label.show()

if __name__ == '__main__':
    one = Site()
    
