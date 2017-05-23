# eliteBonusViolatorsLargeProjectileTurretDamageRole1
#
# Used by:
# Ship: Vargur
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))
