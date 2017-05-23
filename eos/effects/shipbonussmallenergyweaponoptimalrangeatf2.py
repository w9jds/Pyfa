# shipBonusSmallEnergyWeaponOptimalRangeATF2
#
# Used by:
# Ship: Malice
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonusATF2"))
