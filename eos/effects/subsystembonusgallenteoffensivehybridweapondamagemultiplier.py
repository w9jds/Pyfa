# subsystemBonusGallenteOffensiveHybridWeaponDamageMultiplier
#
# Used by:
# Subsystem: Proteus Offensive - Covert Reconfiguration
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("subsystemBonusGallenteOffensive"),
                                  skill="Gallente Offensive Systems")
