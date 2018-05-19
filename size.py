#!/usr/bin/python
# -*- coding: utf-8 -*-

# size.py

import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(300, 500))
            
        self.Show()


if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
