"""
Font file to handle the differences in font calculations between
different wxPython versions
"""

# noinspection PyPackageRequirements
import wx
from service.settings import GeneralSettings

if 'wxMac' in wx.PlatformInfo:
    sizes = (10, 11, 12)
else:
    sizes = (7, 8, 9)

SMALL, NORMAL, BIG = sizes

general_settings = GeneralSettings.getInstance()
font_title_plus_one = wx.Font(
        general_settings.get('fontSize') + 1,
        getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        wx.FONTWEIGHT_BOLD,
)

font_title_plus_two = wx.Font(
        general_settings.get('fontSize') + 2,
        getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        wx.FONTWEIGHT_BOLD,
        False,
)

font_minus_one = wx.Font(
        general_settings.get('fontSize') - 1,
        getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
)

font_plus_one = wx.Font(
        general_settings.get('fontSize') + 1,
        getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
)

font_standard = wx.Font(
        general_settings.get('fontSize'),
        getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
)


font_standard_bold = wx.Font(
        general_settings.get('fontSize'),
        getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        wx.FONTWEIGHT_BOLD,
)

font_console = wx.Font(
        general_settings.get('fontSize'),
        wx.FONTFAMILY_TELETYPE,
        getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
        getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
)
