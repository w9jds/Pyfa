# subsystemBonusGallenteOffensiveDroneHP
#
# Used by:
# Subsystem: Proteus Offensive - Drone Synthesis Projector
effectType = "passive"


def handler(fit, container, context):
    for layer in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), layer,
                                     container.getModifiedItemAttr("subsystemBonusGallenteOffensive"),
                                     skill="Gallente Offensive Systems")
