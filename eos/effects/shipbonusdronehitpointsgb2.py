# shipBonusDroneHitpointsGB2
#
# Used by:
# Variations of ship: Dominix (3 of 3)
# Ship: Nestor
effectType = "passive"


def handler(fit, ship, context):
    for hp_type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     hp_type, ship.getModifiedItemAttr("shipBonusGB2"), skill="Gallente Battleship")
