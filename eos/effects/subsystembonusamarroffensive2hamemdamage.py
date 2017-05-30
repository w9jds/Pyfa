# subsystemBonusAmarrOffensive2HAMEmDamage
#
# Used by:
# Subsystem: Legion Offensive - Assault Optimization
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "emDamage", container.getModifiedItemAttr("subsystemBonusAmarrOffensive2"),
                                    skill="Amarr Offensive Systems")
