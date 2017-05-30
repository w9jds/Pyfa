# subsystemBonusCaldariOffensive3HeavyAssaultMissileVelocity
#
# Used by:
# Subsystem: Tengu Offensive - Accelerated Ejection Bay
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "maxVelocity", container.getModifiedItemAttr("subsystemBonusCaldariOffensive3"),
                                    skill="Caldari Offensive Systems")
