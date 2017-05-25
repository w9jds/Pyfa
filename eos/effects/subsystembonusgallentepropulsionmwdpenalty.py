# subsystemBonusGallentePropulsionMWDPenalty
#
# Used by:
# Subsystem: Proteus Propulsion - Wake Limiter
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                  "signatureRadiusBonus",
                                  container.getModifiedItemAttr("subsystemBonusGallentePropulsion"),
                                  skill="Gallente Propulsion Systems")
