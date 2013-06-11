#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk

import cmdpost


class Terminal():
    def __init__(self, builder):
        self.builder = builder

        self.statusbar_cmd = self.builder.get_object("statusbar_cmd")

        self.entry_cmd = self.builder.get_object("entry_cmd")

        self.textview_cmd = self.builder.get_object("textview_cmd")
        self.cmd_buf = gtk.TextBuffer()
        self.textview_cmd.set_buffer(self.cmd_buf)

        self.command_run = self.builder.get_object("command_run")
        self.command_clear = self.builder.get_object("command_clear")

        self.command_run.connect("clicked", self.command_to_run)
        self.command_clear.connect("clicked", self.command_to_clear)

        self.entry_cmd.connect("activate",self.command_to_run)

    def init_terminal(self, url):
        content, pwd = cmdpost.init_cmd(url)
        #print 'init:',pwd
        self.display_cmd_res('pwd', content, pwd)


    def command_to_clear(self,widget):
        self.entry_cmd.set_text("")


    def display_cmd_res(self, cmd,  content, pwd):
        start = self.cmd_buf.get_start_iter()
        end = self.cmd_buf.get_end_iter()
        text = self.cmd_buf.get_text(start,end)
        if not text:
            text += "%s\n%s " %  ('#' * 68, pwd)
        else:
            text += "%s\n%s\n%s\n%s" %  (cmd ,content ,'+' * 68 ,pwd)
        self.cmd_buf.set_text(text)
        
    
    def command_to_run(self,widget):
        cmd = self.entry_cmd.get_text()
        url = "http://127.0.0.1/null/shell.php"

        content, pwd = cmdpost.run_cmd(url, cmd)
        #print cmd, content, pwd
        self.display_cmd_res(cmd, content, pwd)


if __name__ == '__main__':
    builder = gtk.Builder()
    builder.add_from_file('ui/null.glade')
    win_main = builder.get_object("window_main")
    win_main.connect("destroy",gtk.main_quit)

    Terminal(builder)
    
    gtk.main()
