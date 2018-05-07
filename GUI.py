from inverted_index import word_index
from inverted_table import table
import wx
'''
    sys.path.append('D:\inverted_index\venv\Lib\site-packages')
    #may adjust the system path in order to look for wxPython package
'''

global tab
tab = table()
tab.create_inverted_table('text.txt')
tab.create_inverted_table('text11.txt')

class MyForm(wx.Frame):

    def __init__(self):
        #make frame
        wx.Frame.__init__(self, None, wx.ID_ANY, "Search for words")

        #make panel
        self.panel = wx.Panel(self)
        self.box = wx.BoxSizer(wx.VERTICAL)

        #make static message
        self.message1 = wx.StaticText(self.panel, label = "Type the looking-for words and search")
        self.box.Add(self.message1,0,  wx.ALIGN_CENTRE_HORIZONTAL, 0)

        # make input_box
        self.input_box = wx.TextCtrl(self.panel)
        self.box.Add(self.input_box, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        #search button
        self.button = wx.Button(self.panel, label="Search")
        self.button.Bind(wx.EVT_BUTTON, self.onButton)  # self.Bind(wx.EVT_BUTTON, self.onButton, button)
        self.box.Add(self.button, 0, wx.ALIGN_BOTTOM | wx.CENTER, 0)

        #set the box to panel
        self.panel.SetSizer(self.box)

    # ----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        print("Button pressed!")
        wx.MessageBox(tab.print_table(self.input_box.GetLineText(0)), 'Search Result', wx.OK)

# Run the program
if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()
