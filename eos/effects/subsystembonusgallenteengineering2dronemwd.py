# subsystemBonusGallenteEngineering2DroneMWD
#
# Used by:
# Subsystem: Proteus Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, container, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), "maxVelocity",
                                 container.getModifiedItemAttr("subsystemBonusGallenteEngineering2"),
                                 skill="Gallente Engineering Systems")
