# subsystemBonusMinmatarOffensive2ProjectileWeaponROF
#
# Used by:
# Subsystem: Loki Offensive - Hardpoint Efficiency Configuration
# Subsystem: Loki Offensive - Projectile Scoping Array
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "speed", module.getModifiedItemAttr("subsystemBonusMinmatarOffensive2"),
                                  skill="Minmatar Offensive Systems")
