# eliteBonusViolatorsLargeEnergyTurretDamageRole1
#
# Used by:
# Ship: Paladin
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))
