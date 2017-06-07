# noinspection PyPackageRequirements
import wx

import gui.globalEvents as GE
import gui.mainFrame
from gui.chromeTabs import EVT_NOTEBOOK_PAGE_CHANGED
from gui.utils.helpers_wxPython import Frame


class BlankPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(0, 0))

        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.parent = parent

        self.parent.Bind(EVT_NOTEBOOK_PAGE_CHANGED, self.pageChanged)
        self.SetBackgroundColour(Frame.getBackgroundColor())

        wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=None))

    def Destroy(self, **kwargs):
        self.parent.Unbind(EVT_NOTEBOOK_PAGE_CHANGED, handler=self.pageChanged)
        wx.Panel.Destroy(self)

    def pageChanged(self, event):
        if self.parent.IsActive(self):
            fitID = None
            wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=fitID))

        event.Skip()
