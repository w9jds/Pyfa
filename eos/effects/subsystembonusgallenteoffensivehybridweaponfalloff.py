# subsystemBonusGallenteOffensiveHybridWeaponFalloff
#
# Used by:
# Subsystem: Proteus Offensive - Dissonic Encoding Platform
# Subsystem: Proteus Offensive - Hybrid Propulsion Armature
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "falloff", container.getModifiedItemAttr("subsystemBonusGallenteOffensive"),
                                  skill="Gallente Offensive Systems")
