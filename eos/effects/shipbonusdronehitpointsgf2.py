# shipBonusDroneHitpointsGF2
#
# Used by:
# Ship: Ishkur
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "hp", ship.getModifiedItemAttr("shipBonusGF2"), skill="Gallente Frigate")
