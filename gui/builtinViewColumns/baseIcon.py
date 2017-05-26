# noinspection PyPackageRequirements
import wx
from eos.saveddata.implant import Implant
from eos.saveddata.drone import Drone
from eos.saveddata.module import Module, Slot, Rack
from eos.saveddata.fit import Fit
from gui.viewColumn import ViewColumn


class BaseIcon(ViewColumn):
    name = "Base Icon"

    def __init__(self, fittingView, params):
        ViewColumn.__init__(self, fittingView)
        self.size = 24
        self.maxsize = self.size
        self.mask = wx.LIST_MASK_IMAGE
        self.columnText = ""
        self.shipImage = fittingView.imageList.GetImageIndex("ship_small", "gui")

    def getImageId(self, mod):
        if isinstance(mod, Drone):
            return -1
        elif isinstance(mod, Fit):
            return self.shipImage
        elif isinstance(mod, Rack):
            return -1
        elif isinstance(mod, Implant):
            if mod.character:  # if it has a character as it's parent
                return self.fittingView.imageList.GetImageIndex("character_small", "gui")
            else:
                return self.shipImage
        elif isinstance(mod, Module):
            if mod.isEmpty:
                return self.fittingView.imageList.GetImageIndex("slot_%s_small" % Slot.getName(mod.slot).lower(),
                                                                "gui")
            else:
                return self.loadIconFile(mod.item.icon.iconFile if mod.item.icon else "")

        item = getattr(mod, "item", mod)
        return self.loadIconFile(item.icon.iconFile if item.icon else "")

    def loadIconFile(self, iconFile):
        if iconFile:
            return self.fittingView.imageList.GetImageIndex(iconFile, "icons")
        else:
            return -1


BaseIcon.register()
