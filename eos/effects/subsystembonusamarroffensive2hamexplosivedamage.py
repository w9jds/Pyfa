# subsystemBonusAmarrOffensive2HAMExplosiveDamage
#
# Used by:
# Subsystem: Legion Offensive - Assault Optimization
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "explosiveDamage", container.getModifiedItemAttr("subsystemBonusAmarrOffensive2"),
                                    skill="Amarr Offensive Systems")
