# eliteBonusCommandShipsHeavyMissileExplosionVelocityCS2
#
# Used by:
# Ship: Claymore
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "aoeVelocity", ship.getModifiedItemAttr("eliteBonusCommandShips2"),
                                    skill="Command Ships")
