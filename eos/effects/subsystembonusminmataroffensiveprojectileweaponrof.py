# subsystemBonusMinmatarOffensiveProjectileWeaponROF
#
# Used by:
# Subsystem: Loki Offensive - Covert Reconfiguration
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "speed", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive"),
                                  skill="Minmatar Offensive Systems")
