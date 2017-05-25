# subsystemBonusAmarrEngineeringCapacitorCapacity
#
# Used by:
# Subsystem: Legion Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("capacitorCapacity", container.getModifiedItemAttr("subsystemBonusAmarrEngineering"),
                           skill="Amarr Engineering Systems")
