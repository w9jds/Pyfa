# subsystemBonusMinmatarOffensiveProjectileWeaponMaxRange
#
# Used by:
# Subsystem: Loki Offensive - Turret Concurrence Registry
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive"),
                                  skill="Minmatar Offensive Systems")
