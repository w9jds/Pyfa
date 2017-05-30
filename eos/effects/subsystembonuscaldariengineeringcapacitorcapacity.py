# subsystemBonusCaldariEngineeringCapacitorCapacity
#
# Used by:
# Subsystem: Tengu Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("capacitorCapacity", container.getModifiedItemAttr("subsystemBonusCaldariEngineering"),
                           skill="Caldari Engineering Systems")
