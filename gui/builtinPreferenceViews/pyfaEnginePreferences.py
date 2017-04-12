import logging

import wx
from wx.lib.intctrl import IntCtrl

from service.fit import Fit
from gui.bitmapLoader import BitmapLoader
from gui.preferenceView import PreferenceView
from service.settings import EOSSettings

logger = logging.getLogger(__name__)


class PFFittingEnginePref(PreferenceView):
    title = "Fitting Engine"

    def __init__(self):
        self.dirtySettings = False
        self.engine_settings = EOSSettings.getInstance()

    def refreshPanel(self, fit):
        pass

    # noinspection PyAttributeOutsideInit
    def populatePanel(self, panel):
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.stTitle = wx.StaticText(panel, wx.ID_ANY, self.title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.stTitle.Wrap(-1)
        self.stTitle.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        mainSizer.Add(self.stTitle, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        mainSizer.Add(self.m_staticline1, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.cbGlobalForceReload = wx.CheckBox(panel, wx.ID_ANY, u"Factor in reload time when calculating capacitor usage, damage, and tank.",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbGlobalForceReload, 0, wx.ALL | wx.EXPAND, 5)

        self.cbUniversalAdaptiveArmorHardener = wx.CheckBox(panel, wx.ID_ANY,
                                                            u"When damage profile is Uniform, set Reactive Armor Hardener to match (old behavior).",
                                                            wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbUniversalAdaptiveArmorHardener, 0, wx.ALL | wx.EXPAND, 5)

        self.cbStrictFitting = wx.CheckBox(panel, wx.ID_ANY,
                                           u"Only allow fits that strictly match fitting rules. If this is disabled, fits allowed may not work in EVE." +
                                           u"\n(Only recommended for expert players)",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbStrictFitting, 0, wx.ALL | wx.EXPAND, 5)

        # Search Item Limit
        sizerFireAtPercentCapacitor = wx.BoxSizer(wx.HORIZONTAL)

        self.sizerFireAtPercentCapacitor.Wrap(-1)
        self.sizerFireAtPercentCapacitor = wx.StaticText(
                panel, wx.ID_ANY,
                u"Use capacitor boosters when this percentage is reached: ",
                wx.DefaultPosition, wx.DefaultSize, 0
        )
        sizerFireAtPercentCapacitor.Add(self.sizerFireAtPercentCapacitor, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.editFireAtPercentCapacitor = IntCtrl(panel, max=99, limited=True)
        sizerFireAtPercentCapacitor.Add(self.editFireAtPercentCapacitor, 0, wx.ALL, 5)

        mainSizer.Add(sizerFireAtPercentCapacitor, 0, wx.ALL | wx.EXPAND, 0)

        # Future code once new cap sim is implemented
        '''
        self.cbGlobalForceReactivationTimer = wx.CheckBox( panel, wx.ID_ANY, u"Factor in reactivation timer", wx.DefaultPosition, wx.DefaultSize, 0 )
        mainSizer.Add( self.cbGlobalForceReactivationTimer, 0, wx.ALL|wx.EXPAND, 5 )

        text =  u"   Ignores reactivation timer when calculating capacitor usage,\n   damage, and tank."
        self.cbGlobalForceReactivationTimerText = wx.StaticText( panel, wx.ID_ANY, text, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cbGlobalForceReactivationTimerText.Wrap( -1 )
        self.cbGlobalForceReactivationTimerText.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
        mainSizer.Add( self.cbGlobalForceReactivationTimerText, 0, wx.ALL, 5 )
        '''

        # Future code for mining laser crystal
        '''
        self.cbGlobalMiningSpecialtyCrystal = wx.CheckBox( panel, wx.ID_ANY, u"Factor in reactivation timer", wx.DefaultPosition, wx.DefaultSize, 0 )
        mainSizer.Add( self.cbGlobalMiningSpecialtyCrystal, 0, wx.ALL|wx.EXPAND, 5 )

        text = u"   If enabled, displays the Specialty Crystal mining amount.\n   This is the amount mined when using crystals and mining the matching asteroid."
        self.cbGlobalMiningSpecialtyCrystalText = wx.StaticText( panel, wx.ID_ANY, text, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cbGlobalMiningSpecialtyCrystalText.Wrap( -1 )
        self.cbGlobalMiningSpecialtyCrystalText.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
        mainSizer.Add( self.cbGlobalMiningSpecialtyCrystalText, 0, wx.ALL, 5 )
        '''

        self.sFit = Fit.getInstance()

        self.cbGlobalForceReload.SetValue(self.sFit.serviceFittingOptions["useGlobalForceReload"])
        self.cbGlobalForceReload.Bind(wx.EVT_CHECKBOX, self.OnCBGlobalForceReloadStateChange)

        self.cbUniversalAdaptiveArmorHardener.SetValue(self.engine_settings.get("useStaticAdaptiveArmorHardener"))
        self.cbUniversalAdaptiveArmorHardener.Bind(wx.EVT_CHECKBOX, self.OnCBUniversalAdaptiveArmorHardenerChange)

        self.cbStrictFitting.SetValue(self.engine_settings.get("strictFitting"))
        self.cbStrictFitting.Bind(wx.EVT_CHECKBOX, self.OnCBStrictFittingChange)

        self.editFireAtPercentCapacitor.SetValue(int(self.engine_settings.get("fireAtPercentCapacitor")))
        self.editFireAtPercentCapacitor.Bind(wx.lib.intctrl.EVT_INT, self.OnWindowLeave)

        panel.SetSizer(mainSizer)
        panel.Layout()

    def OnCBGlobalForceReloadStateChange(self, event):
        self.sFit.serviceFittingOptions["useGlobalForceReload"] = self.cbGlobalForceReload.GetValue()

    def OnCBUniversalAdaptiveArmorHardenerChange(self, event):
        self.engine_settings.set("useStaticAdaptiveArmorHardener", self.cbUniversalAdaptiveArmorHardener.GetValue())

    def OnCBStrictFittingChange(self, event):
        self.engine_settings.set("strictFitting", self.cbStrictFitting.GetValue())

    def getImage(self):
        return BitmapLoader.getBitmap("settings_fitting", "gui")

    def OnWindowLeave(self, event):
        self.engine_settings.set('fireAtPercentCapacitor', int(self.editFireAtPercentCapacitor.GetValue()))


PFFittingEnginePref.register()
