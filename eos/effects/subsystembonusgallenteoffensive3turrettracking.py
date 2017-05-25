# subsystemBonusGallenteOffensive3TurretTracking
#
# Used by:
# Subsystem: Proteus Offensive - Dissonic Encoding Platform
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "trackingSpeed", container.getModifiedItemAttr("subsystemBonusGallenteOffensive3"),
                                  skill="Gallente Offensive Systems")
