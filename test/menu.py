#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, os
import pygtk, gtk, gobject

class app:

   def __init__(self):
      window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      window.set_title("TestApp")
      window.set_default_size(320, 240)
      window.connect("destroy", gtk.main_quit)
      window.show_all()


      button = gtk.Button("A Button")
      window.pack_start(button)
      #Create a menu

      menu = gtk.Menu()
      #Fill it with menu items

      menu_item = gtk.MenuItem("A menu item")
      menu.append(menu_item)
      menu_item.show()
      #Make the widget listen for mouse press events, attaching the menu to it.

      button.connect_object("event", self.button_press, menu)
      #Then define the method which handles these events. As is stated in the example in the link, the widget passed to this method is the menu that you want popping up not the widget that is listening for these events.

   def button_press(self, widget, event):
       if event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
           #make widget popup
           widget.popup(None, None, None, event.button, event.time)
           pass

app()
gtk.main()

