# shipBonusDroneDamageMultiplierRookie
#
# Used by:
# Ship: Gnosis
# Ship: Sunesis
# Ship: Taipan
# Ship: Velator
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "damageMultiplier", ship.getModifiedItemAttr("rookieDroneBonus"))
