# subsystemBonusMinmatarPropulsionMaxVelocity
#
# Used by:
# Subsystem: Loki Propulsion - Chassis Optimization
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("subsystemBonusMinmatarPropulsion"),
                           skill="Minmatar Propulsion Systems")
