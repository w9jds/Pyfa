# subsystemBonusAmarrPropulsionMWDPenalty
#
# Used by:
# Subsystem: Legion Propulsion - Wake Limiter
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                  "signatureRadiusBonus", container.getModifiedItemAttr("subsystemBonusAmarrPropulsion"),
                                  skill="Amarr Propulsion Systems")
