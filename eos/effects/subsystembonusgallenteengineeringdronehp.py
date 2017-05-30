# subsystemBonusGallenteEngineeringDroneHP
#
# Used by:
# Subsystem: Proteus Engineering - Augmented Capacitor Reservoir
effectType = "passive"


def handler(fit, container, context):
    for layer in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), layer,
                                     container.getModifiedItemAttr("subsystemBonusGallenteEngineering"),
                                     skill="Gallente Engineering Systems")
