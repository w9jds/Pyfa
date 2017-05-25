# subsystemBonusCaldariOffensive2HybridWeaponDamageMultiplier
#
# Used by:
# Subsystem: Tengu Offensive - Magnetic Infusion Basin
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("subsystemBonusCaldariOffensive2"),
                                  skill="Caldari Offensive Systems")
