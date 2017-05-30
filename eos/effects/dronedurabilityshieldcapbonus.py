# droneDurabilityShieldCapBonus
#
# Used by:
# Modules named like: Drone Durability Enhancer (6 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "shieldCapacity", container.getModifiedItemAttr("hullHpBonus"))
