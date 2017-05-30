# subsystemBonusAmarrPropulsionAfterburnerSpeedFactor
#
# Used by:
# Subsystem: Legion Propulsion - Fuel Catalyst
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "speedFactor", container.getModifiedItemAttr("subsystemBonusAmarrPropulsion"),
                                  skill="Amarr Propulsion Systems")
