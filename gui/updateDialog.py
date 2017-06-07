# =============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
# =============================================================================

# noinspection PyPackageRequirements
import wx
# noinspection PyPackageRequirements
import dateutil.parser
from service.settings import UpdateSettings as svc_UpdateSettings
from gui.utils.helpers_wxPython import Fonts


class UpdateDialog(wx.Dialog):
    def __init__(self, parent, release):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title="Pyfa.fit Update", pos=wx.DefaultPosition,
                           size=wx.Size(400, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.UpdateSettings = svc_UpdateSettings.getInstance()
        self.releaseInfo = release
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        headSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.headingText = wx.StaticText(self, wx.ID_ANY, "Pyfa.fit Update Available!", wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_CENTRE)
        self.headingText.Wrap(-1)
        self.headingText.SetFont(Fonts.getFont("font_title_plus_two"))

        headSizer.Add(self.headingText, 1, wx.ALL, 5)
        mainSizer.Add(headSizer, 0, wx.EXPAND, 5)

        mainSizer.Add(wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL), 0,
                      wx.EXPAND | wx.ALL, 5)

        versionSizer = wx.BoxSizer(wx.HORIZONTAL)

        if self.releaseInfo['prerelease']:
            self.releaseText = wx.StaticText(self, wx.ID_ANY, "Pre-release:", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_RIGHT)
            self.releaseText.SetForegroundColour(wx.Colour(230, 0, 0))
        else:
            self.releaseText = wx.StaticText(self, wx.ID_ANY, "Stable:", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_RIGHT)
        self.releaseText.SetFont(Fonts.getFont("font_plus_one"))

        self.releaseText.Wrap(-1)

        versionSizer.Add(self.releaseText, 1, wx.ALL, 5)

        self.versionText = wx.StaticText(self, wx.ID_ANY, self.releaseInfo['tag_name'], wx.DefaultPosition,
                                         wx.DefaultSize, wx.ALIGN_LEFT)
        self.versionText.Wrap(-1)
        self.versionText.SetFont(Fonts.getFont("font_plus_one"))

        versionSizer.Add(self.versionText, 1, wx.ALL, 5)
        versionSizer.AddSpacer((15, 5), 0, wx.EXPAND, 5)

        mainSizer.Add(versionSizer, 0, wx.EXPAND, 5)
        mainSizer.AddSpacer((0, 5), 0, wx.EXPAND, 5)

        releaseDate = dateutil.parser.parse(self.releaseInfo['published_at'])
        notesSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.notesTextCtrl = wx.TextCtrl(self, wx.ID_ANY, str(releaseDate.date()) + ":\n\n" + self.releaseInfo['body'],
                                         wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_AUTO_URL | wx.TE_MULTILINE | wx.TE_READONLY | wx.DOUBLE_BORDER | wx.TRANSPARENT_WINDOW)
        self.notesTextCtrl.SetFont(Fonts.getFont("font_standard"))

        notesSizer.Add(self.notesTextCtrl, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        mainSizer.Add(notesSizer, 1, wx.EXPAND, 5)

        self.supressCheckbox = wx.CheckBox(self, wx.ID_ANY, "Don't remind me again for this release",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.supressCheckbox.Bind(wx.EVT_CHECKBOX, self.SuppressChange)
        self.supressCheckbox.SetFont(Fonts.getFont("font_standard"))

        mainSizer.Add(self.supressCheckbox, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL), 0,
                      wx.EXPAND | wx.ALL, 5)

        actionSizer = wx.BoxSizer(wx.HORIZONTAL)

        goSizer = wx.BoxSizer(wx.VERTICAL)
        self.downloadButton = wx.Button(self, wx.ID_ANY, "Download", wx.DefaultPosition, wx.DefaultSize, 0)
        self.downloadButton.Bind(wx.EVT_BUTTON, self.OnDownload)
        self.downloadButton.SetFont(Fonts.getFont("font_standard"))
        goSizer.Add(self.downloadButton, 0, wx.ALL, 5)
        actionSizer.Add(goSizer, 1, wx.EXPAND, 5)

        self.closeButton = wx.Button(self, wx.ID_CLOSE)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        self.closeButton.SetFont(Fonts.getFont("font_standard"))
        actionSizer.Add(self.closeButton, 0, wx.ALL, 5)
        mainSizer.Add(actionSizer, 0, wx.EXPAND, 5)

        self.SetSizer(mainSizer)
        self.Layout()

        # Handle use-case of suppressing a release, then a new version becoming available.
        # If that new version is not suppressed, the old version will remain in the preferences and
        # may cause confusion. If this dialog box is popping up for any reason, that mean we can
        # safely reset this setting
        self.UpdateSettings.set('version', None)

        self.Centre(wx.BOTH)

    def OnClose(self, e):
        self.Close()

    def SuppressChange(self, e):
        if self.supressCheckbox.IsChecked():
            self.UpdateSettings.set('version', self.releaseInfo['tag_name'])
        else:
            self.UpdateSettings.set('version', None)

    def OnDownload(self, e):
        wx.LaunchDefaultBrowser('https://github.com/Pyfa-fit/Pyfa-fit/releases/tag/' + self.releaseInfo['tag_name'])
        self.OnClose(e)
