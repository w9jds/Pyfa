# shipBonusDroneHitpointsRookie
#
# Used by:
# Variations of ship: Procurer (2 of 2)
# Ship: Gnosis
# Ship: Sunesis
# Ship: Taipan
# Ship: Velator
effectType = "passive"


def handler(fit, ship, context):
    for hp_type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     hp_type, ship.getModifiedItemAttr("rookieDroneBonus"))
