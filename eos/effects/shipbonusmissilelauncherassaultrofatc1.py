# shipBonusMissileLauncherAssaultROFATC1
#
# Used by:
# Ship: Vangel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Rapid Light",
                                  "speed", ship.getModifiedItemAttr("shipBonusATC1"))
