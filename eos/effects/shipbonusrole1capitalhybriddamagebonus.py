# shipBonusRole1CapitalHybridDamageBonus
#
# Used by:
# Ship: Vehement
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusRole1"))
