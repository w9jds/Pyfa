# smallHybridMaxRangeBonus
#
# Used by:
# Ship: Catalyst
# Ship: Cormorant
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("maxRangeBonus"))
