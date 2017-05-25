# subsystemBonusMinmatarOffensive2ProjectileWeaponDamageMultiplier
#
# Used by:
# Subsystem: Loki Offensive - Turret Concurrence Registry
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive2"),
                                  skill="Minmatar Offensive Systems")
