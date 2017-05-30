# shipBonusDroneStructureHitPointsAB
#
# Used by:
# Ship: Armageddon
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "hp", ship.getModifiedItemAttr("shipBonusAB"), skill="Amarr Battleship")
