# bcLargeHybridTurretCapacitorNeedBonus
#
# Used by:
# Ship: Naga
# Ship: Talos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                     "capacitorNeed", ship.getModifiedItemAttr("bcLargeTurretCap"))
