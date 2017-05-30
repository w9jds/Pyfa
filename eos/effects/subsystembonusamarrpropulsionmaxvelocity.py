# subsystemBonusAmarrPropulsionMaxVelocity
#
# Used by:
# Subsystem: Legion Propulsion - Chassis Optimization
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("subsystemBonusAmarrPropulsion"),
                           skill="Amarr Propulsion Systems")
