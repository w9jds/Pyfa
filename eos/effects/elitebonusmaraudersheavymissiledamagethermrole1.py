# eliteBonusMaraudersHeavyMissileDamageThermRole1
#
# Used by:
# Ship: Golem
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "thermalDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))
