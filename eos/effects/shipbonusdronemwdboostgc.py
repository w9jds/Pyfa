# shipBonusDroneMWDboostGC
#
# Used by:
# Ship: Vexor Navy Issue
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "maxVelocity", ship.getModifiedItemAttr("shipBonusGC"), skill="Gallente Cruiser")
