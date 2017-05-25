# subsystemBonusMinmatarOffensiveProjectileWeaponFalloff
#
# Used by:
# Subsystem: Loki Offensive - Projectile Scoping Array
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "falloff", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive"),
                                  skill="Minmatar Offensive Systems")
