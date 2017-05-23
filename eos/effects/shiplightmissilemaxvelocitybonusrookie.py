# shipLightMissileMaxVelocityBonusRookie
#
# Used by:
# Ship: Taipan
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Light Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("rookieLightMissileVelocity"))
