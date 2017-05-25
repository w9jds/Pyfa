# subsystemBonusMinmatarEngineeringCapacitorCapacity
#
# Used by:
# Subsystem: Loki Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("capacitorCapacity", container.getModifiedItemAttr("subsystemBonusMinmatarEngineering"),
                           skill="Minmatar Engineering Systems")
