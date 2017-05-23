# subsystemBonusGallentePropulsion2WarpCapacitor
#
# Used by:
# Subsystem: Proteus Propulsion - Gravitational Capacitor
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("warpCapacitorNeed", module.getModifiedItemAttr("subsystemBonusGallentePropulsion2"),
                           skill="Gallente Propulsion Systems")
