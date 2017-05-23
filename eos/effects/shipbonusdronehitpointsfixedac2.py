# shipBonusDroneHitpointsFixedAC2
#
# Used by:
# Variations of ship: Arbitrator (3 of 3)
effectType = "passive"


def handler(fit, ship, context):
    for hp_type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     hp_type, ship.getModifiedItemAttr("shipBonusAC2"), skill="Amarr Cruiser")
