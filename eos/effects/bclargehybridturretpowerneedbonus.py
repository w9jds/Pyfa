# bcLargeHybridTurretPowerNeedBonus
#
# Used by:
# Ship: Naga
# Ship: Talos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                     "power", ship.getModifiedItemAttr("bcLargeTurretPower"))
