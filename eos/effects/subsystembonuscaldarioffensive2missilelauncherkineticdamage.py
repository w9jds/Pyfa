# subsystemBonusCaldariOffensive2MissileLauncherKineticDamage
#
# Used by:
# Subsystem: Tengu Offensive - Accelerated Ejection Bay
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "kineticDamage", module.getModifiedItemAttr("subsystemBonusCaldariOffensive2"),
                                    skill="Caldari Offensive Systems")
