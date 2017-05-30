# subsystemBonusGallenteOffensive2HybridWeaponDamageMultiplier
#
# Used by:
# Variations of subsystem: Proteus Offensive - Dissonic Encoding Platform (3 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("subsystemBonusGallenteOffensive2"),
                                  skill="Gallente Offensive Systems")
