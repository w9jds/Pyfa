# subsystemBonusGallentePropulsionWarpSpeed
#
# Used by:
# Subsystem: Proteus Propulsion - Gravitational Capacitor
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("baseWarpSpeed", module.getModifiedItemAttr("subsystemBonusGallentePropulsion"),
                           skill="Gallente Propulsion Systems")
