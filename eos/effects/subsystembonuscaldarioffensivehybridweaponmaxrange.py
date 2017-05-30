# subsystemBonusCaldariOffensiveHybridWeaponMaxRange
#
# Used by:
# Subsystem: Tengu Offensive - Magnetic Infusion Basin
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusCaldariOffensive"),
                                  skill="Caldari Offensive Systems")
