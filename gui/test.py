#coding=utf-8
import wx
import wx.html
import os
from fun import login
text1='''
<html>
<head>
<title>Page title</title>
</head>
<body>
<p align="center" id="firstpara" style="color: crimson">
        This is hello
        </p>
</body>
</html>

'''
text2='''
<html>
<head>
<title>Page title</title>
</head>
<body>
<p align="center" id="firstpara" style="color: crimson">
        This is the
</body>
</html>

'''
text3='''
<html>
<head>
<title>Page title</title>
</head>
<body>
<p align="center" id="firstpara" style="color: crimson">
        This is world
</body>
</html>

'''
class Myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1)
        self.all_SizerItem=[]
        self.panel=wx.Panel(self,-1)#主panel
        self.hox=wx.BoxSizer(wx.VERTICAL)#垂直布局
        self.create_button()#第一行button行
        self.create_tap_item()#第二行item行
        self.panel.SetSizer(self.hox)
        self.hox.Layout()
        self.create_Menu()
        self.create_Toolbar()
    def create_tap_item(self):
        button_item=["hello","the","world"]
        for i,each in enumerate(button_item):
            child_panel = wx.Panel(self.panel, -1)#新建子panel
            panel_child_hox=wx.BoxSizer(wx.HORIZONTAL)
            html = wx.html.HtmlWindow(child_panel)
            if i==0:
                text=text1
            elif i==1:
                text=text2
            else:
                text=text3
            html.SetPage(text)
            # html.SetBackgroundColour(wx.RED)
            panel_child_hox.Add(html,1,wx.EXPAND|wx.ALL,0)
            child_panel.SetSizer(panel_child_hox)
            self.hox.Add(child_panel,1,wx.EXPAND|wx.ALL,20)#把item下的子panel添加Sizer
            if i!=0:
                self.hox.Hide(child_panel)#隐藏不是第一列的item
            self.all_SizerItem.append((each,child_panel))#将所有的item下的子panel添加进列表
    def create_button(self):
        child_panel = wx.Panel(self.panel, -1)#创建一个子panel
        self.hox_button = wx.BoxSizer(wx.HORIZONTAL)  # 按钮水平布局
        button = wx.Button(child_panel, -1, "hello")
        button1 = wx.Button(child_panel, -1, "the")
        button2 = wx.Button(child_panel, -1, "world")
        self.hox_button.Add(button, proportion=0, flag=wx.ALL, border=0)
        self.hox_button.Add(button1, proportion=0, flag=wx.ALL, border=0)
        self.hox_button.Add(button2, proportion=0, flag=wx.ALL, border=0)
        child_panel.SetSizer(self.hox_button)
        self.Bind(wx.EVT_BUTTON, self.Register)
        self.hox.Add(child_panel,0,wx.EXPAND)#把新建的子panel添加Size
    def create_Toolbar(self):
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        add = toolbar.AddSimpleTool(wx.NewId(), wx.Bitmap("./pic/folder.png"), "New", "long help for 'New'")
        edit = toolbar.AddSimpleTool(wx.NewId(), wx.Bitmap("./pic/folder.png"), "Edit", "long help for 'Edit'")
        toolbar.Realize()
    def create_Menu(self):
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuItem = menu1.Append(-1, "&Quit", "&Quit")
        menuItem1 = menu1.Append(-1, "&Quit1", "&Quit1")
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)
    def Register(self,event):
        label=wx.FindWindowById(event.GetId()).GetLabelText()
        for each,item in self.all_SizerItem:
            if each!=label:
                self.hox.Hide(item)#如果不是button label显示的item隐藏
            else:
                check_item=item
        self.hox.Show(check_item)
        self.panel.Layout()#重新布局

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=Myframe()
    frame.Show(True)
    app.MainLoop()