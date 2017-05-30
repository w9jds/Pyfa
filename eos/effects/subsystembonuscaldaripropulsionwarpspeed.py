# subsystemBonusCaldariPropulsionWarpSpeed
#
# Used by:
# Subsystem: Tengu Propulsion - Gravitational Capacitor
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("baseWarpSpeed", container.getModifiedItemAttr("subsystemBonusCaldariPropulsion"),
                           skill="Caldari Propulsion Systems")
