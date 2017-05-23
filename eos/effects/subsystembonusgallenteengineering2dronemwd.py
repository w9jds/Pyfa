# subsystemBonusGallenteEngineering2DroneMWD
#
# Used by:
# Subsystem: Proteus Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), "maxVelocity",
                                 module.getModifiedItemAttr("subsystemBonusGallenteEngineering2"),
                                 skill="Gallente Engineering Systems")
