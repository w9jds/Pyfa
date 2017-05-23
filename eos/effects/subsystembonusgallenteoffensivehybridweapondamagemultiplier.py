# subsystemBonusGallenteOffensiveHybridWeaponDamageMultiplier
#
# Used by:
# Subsystem: Proteus Offensive - Covert Reconfiguration
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", module.getModifiedItemAttr("subsystemBonusGallenteOffensive"),
                                  skill="Gallente Offensive Systems")
