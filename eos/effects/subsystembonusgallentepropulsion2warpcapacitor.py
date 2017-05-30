# subsystemBonusGallentePropulsion2WarpCapacitor
#
# Used by:
# Subsystem: Proteus Propulsion - Gravitational Capacitor
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("warpCapacitorNeed", container.getModifiedItemAttr("subsystemBonusGallentePropulsion2"),
                           skill="Gallente Propulsion Systems")
