# shipBonusSmallHybridMaxRangeATF2
#
# Used by:
# Ship: Utu
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonusATF2"))
