# subsystemBonusCaldariOffensive3HeavyMissileVelocity
#
# Used by:
# Subsystem: Tengu Offensive - Accelerated Ejection Bay
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "maxVelocity", module.getModifiedItemAttr("subsystemBonusCaldariOffensive3"),
                                    skill="Caldari Offensive Systems")
