# subsystemBonusCaldariPropulsion2WarpCapacitor2
#
# Used by:
# Subsystem: Tengu Propulsion - Gravitational Capacitor
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("warpCapacitorNeed", container.getModifiedItemAttr("subsystemBonusCaldariPropulsion2"),
                           skill="Caldari Propulsion Systems")
