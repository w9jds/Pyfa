# noinspection PyPackageRequirements
import wx

from service.fit import Fit
import gui.globalEvents as GE
import gui.mainFrame


class NotesView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Establish instances
        self.sFit = Fit.getInstance()

        self.lastFitId = None
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.editNotes = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.BORDER_NONE, )
        mainSizer.Add(self.editNotes, 1, wx.EXPAND)
        self.SetSizer(mainSizer)
        self.mainFrame.Bind(GE.FIT_CHANGED, self.fitChanged)
        self.Bind(wx.EVT_TEXT, self.onText)
        self.saveTimer = wx.Timer(self)
        self.saveTimer.fitID = None
        self.Bind(wx.EVT_TIMER, self.delayedSave, self.saveTimer)

    def fitChanged(self, event):
        fit = self.sFit.getFit(event.fitID)

        self.saveTimer.Stop()  # cancel any pending timers

        self.Parent.Parent.DisablePage(self, not fit or fit.isStructure)

        # when switching fits, ensure that we save the notes for the previous fit
        if self.saveTimer.fitID and self.saveTimer.fitID != event.fitID:
            self.sFit.editNotes(self.saveTimer.fitID, self.editNotes.GetValue())

        if event.fitID is None:
            self.saveTimer.fitID = None
        else:
            self.editNotes.SetValue(fit.notes or "")
            self.saveTimer.fitID = event.fitID

        event.Skip()
        return

    def onText(self, event):
        fitID = getattr(event, 'fitID', None)
        if fitID:
            # delay the save so we're not writing to sqlite on every keystroke
            self.saveTimer.Stop()  # cancel the existing timer
            self.saveTimer.Start(1000, True)
            self.saveTimer.fitID = fitID

    def delayedSave(self, event):
        fit = self.sFit.getFit(self.saveTimer.fitID)
        if fit:
            self.sFit.editNotes(self.saveTimer.fitID, self.editNotes.GetValue())

        self.saveTimer.fitID = None
