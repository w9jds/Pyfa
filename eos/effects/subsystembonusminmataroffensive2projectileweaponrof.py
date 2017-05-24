# subsystemBonusMinmatarOffensive2ProjectileWeaponROF
#
# Used by:
# Subsystem: Loki Offensive - Hardpoint Efficiency Configuration
# Subsystem: Loki Offensive - Projectile Scoping Array
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "speed", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive2"),
                                  skill="Minmatar Offensive Systems")
