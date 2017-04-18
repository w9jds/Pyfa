# coding: utf-8
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
from gui.viewColumn import ViewColumn
import gui.mainFrame
from eos.staticData import Slot


class SlotColumn(ViewColumn):
    name = "Slot"

    def __init__(self, fittingView, params):
        ViewColumn.__init__(self, fittingView)

        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.columnText = ""
        self.shipImage = fittingView.imageList.GetImageIndex("ship_small", "gui")
        self.mask = wx.LIST_MASK_TEXT
        self.projectedView = isinstance(fittingView, gui.projectedView.ProjectedView)

    def getText(self, stuff):
        slot_name = Slot.getName(stuff.slot)

        if slot_name:
            slot_icon = self.fittingView.imageList.GetImageIndex("slot_%s_small" % slot_name.lower(), "gui")
            if not slot_icon:
                return slot_name

        return ""

    def getImageId(self, stuff):
        slot_name = Slot.getName(stuff.slot)

        if slot_name:
            slot_icon = self.fittingView.imageList.GetImageIndex("slot_%s_small" % slot_name.lower(), "gui")
        else:
            slot_icon = -1

        return slot_icon


SlotColumn.register()
