in/env python

# example notebook.py

import gtk

class NotebookExample:
    # This method rotates the position of the tabs
    def rotate_book(self, button, notebook):
        notebook.set_tab_pos((notebook.get_tab_pos()+1) %4)

    # Add/Remove the page tabs and the borders
    def tabsborder_book(self, button, notebook):
        tval = gtk.FALSE
        bval = gtk.FALSE
        if self.show_tabs == gtk.FALSE:
            tval = gtk.TRUE 
        if self.show_border == gtk.FALSE:
            bval = gtk.TRUE

        notebook.set_show_tabs(tval)
        self.show_tabs = tval
        notebook.set_show_border(bval)
        self.show_border = bval

    # Remove a page from the notebook
    def remove_book(self, button, notebook):
        page = notebook.get_current_page()
        notebook.remove_page(page)
        # Need to refresh the widget -- 
        # This forces the widget to redraw itself.
        notebook.draw((0,0,-1,-1))

    def delete(self, widget, event=None):
        gtk.mainquit()
        return gtk.FALSE

    def __init__(self):
        window = gtk.GtkWindow(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.delete)
        window.set_border_width(10)

        table = gtk.GtkTable(3,6,gtk.FALSE)
        window.add(table)

        # Create a new notebook, place the position of the tabs
        notebook = gtk.GtkNotebook()
        notebook.set_tab_pos(gtk.POS_TOP)
        table.attach(notebook, 0,6,0,1)
        notebook.show()
        self.show_tabs = gtk.TRUE
        self.show_border = gtk.TRUE

        # Let's append a bunch of pages to the notebook
        for i in range(5):
            bufferf = "Append Frame %d" % (i+1)
            bufferl = "Page %d" % (i+1)

            frame = gtk.GtkFrame(bufferf)
            frame.set_border_width(10)
            frame.set_usize(100, 75)
            frame.show()

            label = gtk.GtkLabel(bufferf)
            frame.add(label)
            label.show()

            label = gtk.GtkLabel(bufferl)
            notebook.append_page(frame, label)
      
        # Now let's add a page to a specific spot
        checkbutton = gtk.GtkCheckButton("Check me please!")
        checkbutton.set_usize(100, 75)
        checkbutton.show ()

        label = gtk.GtkLabel("Add page")
        notebook.insert_page(checkbutton, label, 2)

        # Now finally let's prepend pages to the notebook
        for i in range(5):
            bufferf = "Prepend Frame %d" % (i+1)
            bufferl = "PPage %d" % (i+1)

            frame = gtk.GtkFrame(bufferf)
            frame.set_border_width(10)
            frame.set_usize(100, 75)
            frame.show()

            label = gtk.GtkLabel(bufferf)
            frame.add(label)
            label.show()

            label = gtk.GtkLabel(bufferl)
            notebook.prepend_page(frame, label)
    
        # Set what page to start at (page 4)
        notebook.set_page(3)

        # Create a bunch of buttons
        button = gtk.GtkButton("close")
        button.connect("clicked", self.delete)
        table.attach(button, 0,1,1,2)
        button.show()

        button = gtk.GtkButton("next page")
        button.connect("clicked", notebook.next_page)
        table.attach(button, 1,2,1,2)
        button.show()

        button = gtk.GtkButton("prev page")
        button.connect("clicked", notebook.prev_page)
        table.attach(button, 2,3,1,2)
        button.show()

        button = gtk.GtkButton("tab position")
        button.connect("clicked", self.rotate_book, notebook)
        table.attach(button, 3,4,1,2)
        button.show()

        button = gtk.GtkButton("tabs/border on/off")
        button.connect("clicked", self.tabsborder_book, notebook)
        table.attach(button, 4,5,1,2)
        button.show()

        button = gtk.GtkButton("remove page")
        button.connect("clicked", self.remove_book, notebook)
        table.attach(button, 5,6,1,2)
        button.show()

        table.show()
        window.show()

def main():
    gtk.mainloop()
    return 0

if __name__ == "__main__":
    NotebookExample()
    main()
