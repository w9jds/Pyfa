# subsystemBonusMinmatarPropulsionAfterburnerSpeedFactor
#
# Used by:
# Subsystem: Loki Propulsion - Fuel Catalyst
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "speedFactor", container.getModifiedItemAttr("subsystemBonusMinmatarPropulsion"),
                                  skill="Minmatar Propulsion Systems")
