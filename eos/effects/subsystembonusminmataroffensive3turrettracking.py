# subsystemBonusMinmatarOffensive3TurretTracking
#
# Used by:
# Subsystem: Loki Offensive - Turret Concurrence Registry
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "trackingSpeed", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive3"),
                                  skill="Minmatar Offensive Systems")
