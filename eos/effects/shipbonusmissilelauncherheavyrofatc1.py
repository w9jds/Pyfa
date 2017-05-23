# shipBonusMissileLauncherHeavyROFATC1
#
# Used by:
# Ship: Vangel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy",
                                  "speed", ship.getModifiedItemAttr("shipBonusATC1"))
