# subsystemBonusCaldariPropulsionAfterburnerSpeedFactor
#
# Used by:
# Subsystem: Tengu Propulsion - Fuel Catalyst
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "speedFactor", container.getModifiedItemAttr("subsystemBonusCaldariPropulsion"),
                                  skill="Caldari Propulsion Systems")
