# bcLargeProjectileTurretCPUNeedBonus
#
# Used by:
# Ship: Tornado
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                     "cpu", ship.getModifiedItemAttr("bcLargeTurretCPU"))
