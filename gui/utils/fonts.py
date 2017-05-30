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


class Fonts(object):
    @staticmethod
    def getFont(FontType):
        size, family, style, weight = getattr(Fonts, FontType, Fonts.font_standard)
        return wx.Font(size, family, style, weight)

    general_settings = GeneralSettings.getInstance()

    font_standard = (
            general_settings.get('fontSize'),
            getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
    )

    font_title_plus_one = (
            general_settings.get('fontSize') + 1,
            getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            wx.FONTWEIGHT_BOLD,
    )

    font_title_plus_two = (
            general_settings.get('fontSize') + 2,
            getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            wx.FONTWEIGHT_BOLD,
    )

    font_minus_one = (
            general_settings.get('fontSize') - 1,
            getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
    )

    font_plus_one = (
            general_settings.get('fontSize') + 1,
            getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
    )

    font_standard_bold = (
            general_settings.get('fontSize'),
            getattr(wx, 'FONTFAMILY_' + general_settings.get('fontType'), wx.FONTFAMILY_DEFAULT),
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            wx.FONTWEIGHT_BOLD,
    )

    font_console = (
            general_settings.get('fontSize'),
            wx.FONTFAMILY_TELETYPE,
            getattr(wx, 'FONTSTYLE_' + general_settings.get('fontStyle'), wx.FONTSTYLE_NORMAL),
            getattr(wx, 'FONTWEIGHT_' + general_settings.get('fontWeight'), wx.FONTWEIGHT_NORMAL),
    )
