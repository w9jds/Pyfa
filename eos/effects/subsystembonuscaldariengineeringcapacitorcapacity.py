# subsystemBonusCaldariEngineeringCapacitorCapacity
#
# Used by:
# Subsystem: Tengu Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("capacitorCapacity", module.getModifiedItemAttr("subsystemBonusCaldariEngineering"),
                           skill="Caldari Engineering Systems")
