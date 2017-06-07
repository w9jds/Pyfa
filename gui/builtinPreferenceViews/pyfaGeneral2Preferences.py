# noinspection PyPackageRequirements
import wx
from wx.lib.intctrl import IntCtrl

from gui.preferenceView import PreferenceView
from gui.bitmapLoader import BitmapLoader

import gui.mainFrame
import gui.globalEvents as GE
from service.settings import SettingsProvider, GeneralSettings
from service.fit import Fit
from service.price import Price
from gui.utils.helpers_wxPython import Fonts


class PFGeneral2Pref(PreferenceView):
    title = "General (2)"

    def populatePrefPanel(self, panel):
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.dirtySettings = False
        self.openFitsSettings = SettingsProvider.getInstance().getSettings("pyfaPrevOpenFits",
                                                                           {"enabled": False, "pyfaOpenFits": []})
        self.sFit = Fit.getInstance()
        self.generalSettings = GeneralSettings.getInstance()

        helpCursor = wx.StockCursor(wx.CURSOR_QUESTION_ARROW)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.stTitle = wx.StaticText(panel, wx.ID_ANY, self.title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.stTitle.Wrap(-1)
        self.stTitle.SetFont(Fonts.getFont("font_title_plus_one"))

        mainSizer.Add(self.stTitle, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        mainSizer.Add(self.m_staticline1, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.cbFitColorSlots = wx.CheckBox(panel, wx.ID_ANY, u"Color fitting view by slot", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        mainSizer.Add(self.cbFitColorSlots, 0, wx.ALL | wx.EXPAND, 5)

        self.cbGaugeAnimation = wx.CheckBox(panel, wx.ID_ANY, u"Animate gauges", wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbGaugeAnimation, 0, wx.ALL | wx.EXPAND, 5)

        # Font size
        fontSizeSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.stFontText = wx.StaticText(panel, wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stFontText.Wrap(-1)
        fontSizeSizer.Add(self.stFontText, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chFontSize = wx.Choice(panel, choices=['6', '7', '8', '9', '10', '11', '12'])
        fontSizeSizer.Add(self.chFontSize, 1, wx.ALL | wx.EXPAND, 5)

        self.stFontText = wx.StaticText(panel, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stFontText.Wrap(-1)
        fontSizeSizer.Add(self.stFontText, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chFontType = wx.Choice(panel, choices=['DEFAULT', 'DECORATIVE', 'MODERN', 'ROMAN', 'SCRIPT', 'SWISS', 'TELETYPE'])
        fontSizeSizer.Add(self.chFontType, 1, wx.ALL | wx.EXPAND, 5)

        self.stFontText = wx.StaticText(panel, wx.ID_ANY, u"Style:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stFontText.Wrap(-1)
        fontSizeSizer.Add(self.stFontText, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chFontStyle = wx.Choice(panel, choices=['NORMAL', 'ITALIC', 'SLANT'])
        fontSizeSizer.Add(self.chFontStyle, 1, wx.ALL | wx.EXPAND, 5)

        self.stFontText = wx.StaticText(panel, wx.ID_ANY, u"Weight:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stFontText.Wrap(-1)
        fontSizeSizer.Add(self.stFontText, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chFontWeight = wx.Choice(panel, choices=['NORMAL', 'BOLD', 'LIGHT'])
        fontSizeSizer.Add(self.chFontWeight, 1, wx.ALL | wx.EXPAND, 5)

        mainSizer.Add(fontSizeSizer, 0, wx.ALL | wx.EXPAND, 0)

        # Background/Text Colors
        bgColorSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.stBackgroundColor = wx.StaticText(panel, wx.ID_ANY, u"Background Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stBackgroundColor.Wrap(-1)
        bgColorSizer.Add(self.stBackgroundColor, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chBackgroundColor = wx.Choice(panel, choices=['BLACK', 'BLUE', 'CYAN', 'GREEN', 'YELLOW', 'LIGHT_GREY', 'RED', 'WHITE', 'SYS_COLOUR_SCROLLBAR', 'SYS_COLOUR_BACKGROUND', 'SYS_COLOUR_ACTIVECAPTION', 'SYS_COLOUR_INACTIVECAPTION', 'SYS_COLOUR_MENU', 'SYS_COLOUR_WINDOW', 'SYS_COLOUR_WINDOWFRAME', 'SYS_COLOUR_MENUTEXT', 'SYS_COLOUR_WINDOWTEXT', 'SYS_COLOUR_CAPTIONTEXT', 'SYS_COLOUR_ACTIVEBORDER', 'SYS_COLOUR_INACTIVEBORDER', 'SYS_COLOUR_APPWORKSPACE', 'SYS_COLOUR_HIGHLIGHT', 'SYS_COLOUR_HIGHLIGHTTEXT', 'SYS_COLOUR_BTNFACE', 'SYS_COLOUR_BTNSHADOW', 'SYS_COLOUR_GRAYTEXT', 'SYS_COLOUR_BTNTEXT', 'SYS_COLOUR_INACTIVECAPTIONTEXT', 'SYS_COLOUR_BTNHIGHLIGHT', 'SYS_COLOUR_3DDKSHADOW', 'SYS_COLOUR_3DLIGHT', 'SYS_COLOUR_INFOTEXT', 'SYS_COLOUR_INFOBK', 'SYS_COLOUR_LISTBOX', 'SYS_COLOUR_HOTLIGHT', 'SYS_COLOUR_GRADIENTACTIVECAPTION', 'SYS_COLOUR_GRADIENTINACTIVECAPTION', 'SYS_COLOUR_MENUHILIGHT', 'SYS_COLOUR_MENUBAR', 'SYS_COLOUR_LISTBOXTEXT', 'SYS_COLOUR_LISTBOXHIGHLIGHTTEXT', 'SYS_COLOUR_MAX', 'SYS_COLOUR_DESKTOP', 'SYS_COLOUR_3DFACE', 'SYS_COLOUR_3DSHADOW', 'SYS_COLOUR_BTNHILIGHT', 'SYS_COLOUR_3DHIGHLIGHT', 'SYS_COLOUR_3DHILIGHT', 'SYS_COLOUR_FRAMEBK'])
        bgColorSizer.Add(self.chBackgroundColor, 1, wx.ALL | wx.EXPAND, 5)

        mainSizer.Add(bgColorSizer, 0, wx.ALL | wx.EXPAND, 0)

        # Text Colors
        txtColorSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.stBackgroundColor = wx.StaticText(panel, wx.ID_ANY, u"Text Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stBackgroundColor.Wrap(-1)
        txtColorSizer.Add(self.stBackgroundColor, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chForegroundColor = wx.Choice(panel, choices=['BLACK', 'BLUE', 'CYAN', 'GREEN', 'YELLOW', 'LIGHT_GREY', 'RED', 'WHITE', 'SYS_COLOUR_SCROLLBAR', 'SYS_COLOUR_BACKGROUND', 'SYS_COLOUR_ACTIVECAPTION', 'SYS_COLOUR_INACTIVECAPTION', 'SYS_COLOUR_MENU', 'SYS_COLOUR_WINDOW', 'SYS_COLOUR_WINDOWFRAME', 'SYS_COLOUR_MENUTEXT', 'SYS_COLOUR_WINDOWTEXT', 'SYS_COLOUR_CAPTIONTEXT', 'SYS_COLOUR_ACTIVEBORDER', 'SYS_COLOUR_INACTIVEBORDER', 'SYS_COLOUR_APPWORKSPACE', 'SYS_COLOUR_HIGHLIGHT', 'SYS_COLOUR_HIGHLIGHTTEXT', 'SYS_COLOUR_BTNFACE', 'SYS_COLOUR_BTNSHADOW', 'SYS_COLOUR_GRAYTEXT', 'SYS_COLOUR_BTNTEXT', 'SYS_COLOUR_INACTIVECAPTIONTEXT', 'SYS_COLOUR_BTNHIGHLIGHT', 'SYS_COLOUR_3DDKSHADOW', 'SYS_COLOUR_3DLIGHT', 'SYS_COLOUR_INFOTEXT', 'SYS_COLOUR_INFOBK', 'SYS_COLOUR_LISTBOX', 'SYS_COLOUR_HOTLIGHT', 'SYS_COLOUR_GRADIENTACTIVECAPTION', 'SYS_COLOUR_GRADIENTINACTIVECAPTION', 'SYS_COLOUR_MENUHILIGHT', 'SYS_COLOUR_MENUBAR', 'SYS_COLOUR_LISTBOXTEXT', 'SYS_COLOUR_LISTBOXHIGHLIGHTTEXT', 'SYS_COLOUR_MAX', 'SYS_COLOUR_DESKTOP', 'SYS_COLOUR_3DFACE', 'SYS_COLOUR_3DSHADOW', 'SYS_COLOUR_BTNHILIGHT', 'SYS_COLOUR_3DHIGHLIGHT', 'SYS_COLOUR_3DHILIGHT', 'SYS_COLOUR_FRAMEBK'])
        txtColorSizer.Add(self.chForegroundColor, 1, wx.ALL | wx.EXPAND, 5)

        mainSizer.Add(txtColorSizer, 0, wx.ALL | wx.EXPAND, 0)

        self.m_staticline = wx.StaticLine(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        mainSizer.Add(self.m_staticline, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.btnApply = wx.Button(panel, wx.ID_ANY, u"Apply Settings", wx.DefaultPosition, wx.DefaultSize, 0)

        btnSizer.Add(self.btnApply, 0, wx.ALL, 5)

        mainSizer.Add(btnSizer, 0, wx.EXPAND, 5)

        self.cbFitColorSlots.SetValue(self.sFit.serviceFittingOptions["colorFitBySlot"] or False)
        self.cbGaugeAnimation.SetValue(self.sFit.serviceFittingOptions["enableGaugeAnimation"])
        self.chFontSize.SetStringSelection(unicode(self.generalSettings.get("fontSize")))
        self.chFontType.SetStringSelection(self.generalSettings.get("fontType"))
        self.chFontStyle.SetStringSelection(self.generalSettings.get("fontStyle"))
        self.chFontWeight.SetStringSelection(self.generalSettings.get("fontWeight"))
        self.chBackgroundColor.SetStringSelection(self.generalSettings.get("colorBackground"))
        self.chForegroundColor.SetStringSelection(self.generalSettings.get("colorForeground"))

        self.cbFitColorSlots.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbGaugeAnimation.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.chFontSize.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)
        self.chFontType.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)
        self.chFontStyle.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)
        self.chFontWeight.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)
        self.chBackgroundColor.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)
        self.chForegroundColor.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)
        self.btnApply.Bind(wx.EVT_BUTTON, self.OnWindowLeave)

        panel.SetSizer(mainSizer)
        panel.Layout()

    def getImage(self):
        return BitmapLoader.getBitmap("prefs_settings", "gui")

    def OnWindowLeave(self, event):
        self.sFit.serviceFittingOptions["colorFitBySlot"] = self.cbFitColorSlots.GetValue()
        self.sFit.serviceFittingOptions["enableGaugeAnimation"] = self.cbGaugeAnimation.GetValue()

        # Font settings
        self.generalSettings.set('fontSize', int(self.chFontSize.GetString(self.chFontSize.GetSelection())))
        self.generalSettings.set('fontType', self.chFontType.GetString(self.chFontType.GetSelection()))
        self.generalSettings.set('fontStyle', self.chFontStyle.GetString(self.chFontStyle.GetSelection()))
        self.generalSettings.set('fontWeight', self.chFontWeight.GetString(self.chFontWeight.GetSelection()))

        # Background & foreground color settings
        self.generalSettings.set('colorBackground', self.chBackgroundColor.GetString(self.chBackgroundColor.GetSelection()))
        self.generalSettings.set('colorForeground', self.chForegroundColor.GetString(self.chForegroundColor.GetSelection()))

        fitID = self.mainFrame.getActiveFit()
        if fitID:
            fit = self.sFit.getFit(fitID)
            self.sFit.recalc(fit)
            wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=fitID))
        event.Skip()


PFGeneral2Pref.register()
