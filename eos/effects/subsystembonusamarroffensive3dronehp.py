# subsystemBonusAmarrOffensive3DroneHP
#
# Used by:
# Subsystem: Legion Offensive - Drone Synthesis Projector
effectType = "passive"


def handler(fit, container, context):
    for layer in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), layer,
                                     container.getModifiedItemAttr("subsystemBonusAmarrOffensive3"),
                                     skill="Amarr Offensive Systems")
