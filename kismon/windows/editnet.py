from gi.repository import Gtk


class EditNetWindow(Gtk.Dialog):
    '''
    Dialog for editing a network in the network list.
    
    This is necessary because the network list is constantly updating while 
    the user is trying to make changes which can cause frustrating behavior
    like lost input.
    '''
    
    def __init__(self, mac, network):
        super().__init__(title="My Dialog", flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.result = ""
        self.set_default_size(150, 100)
        self.connect("response", self.on_response)
        box = self.get_content_area()

        # Title
        net = Gtk.Label(label=f"{mac}")
        ssid = Gtk.Label(label=f"{network['ssid']}")
        box.add(net)
        box.add(ssid)
        
        # Comment
        comment_box = Gtk.Box(spacing=6)
        label = Gtk.Label(label="Comment")
        self.comment = Gtk.Entry()
        self.comment.set_text(network['comment'])
        comment_box.add(label)
        comment_box.add(self.comment)
        box.add(comment_box)
        
        # CodeName
        codename_box = Gtk.Box(spacing=6)
        label = Gtk.Label(label="CodeName")
        self.codename = Gtk.Entry()
        self.codename.set_text(network['codename'])
        codename_box.add(label)
        codename_box.add(self.codename)
        box.add(codename_box)

        self.show_all()
        
    def on_response(self, widget, response_id):
        '''
        Used to save user input in a dict so the place that spawned the dialog can 
        see what the inputs were.
        '''
        self.result = {
            "comment":  self.comment.get_text (),
            "codename": self.codename.get_text()
        }
        
    def get_result(self):
        return self.result