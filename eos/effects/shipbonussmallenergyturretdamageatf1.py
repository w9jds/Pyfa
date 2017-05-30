# shipBonusSmallEnergyTurretDamageATF1
#
# Used by:
# Ship: Malice
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusATF1"))
