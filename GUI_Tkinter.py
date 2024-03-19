import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="¡Hola, Raspberry Pi!")
        self.panel = wx.Panel(self)

        label = wx.StaticText(self.panel, label="¡Hola, Raspberry Pi!")
        button = wx.Button(self.panel, label="Presioname")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label, 0, wx.ALL, 10)
        sizer.Add(button, 0, wx.ALL, 10)
        self.panel.SetSizer(sizer)

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
