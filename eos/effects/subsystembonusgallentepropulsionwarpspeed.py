# subsystemBonusGallentePropulsionWarpSpeed
#
# Used by:
# Subsystem: Proteus Propulsion - Gravitational Capacitor
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("baseWarpSpeed", container.getModifiedItemAttr("subsystemBonusGallentePropulsion"),
                           skill="Gallente Propulsion Systems")
