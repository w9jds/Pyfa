# Not used by any item
effectType = "passive"


def handler(fit, ship, context):
    for hp_type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     hp_type, ship.getModifiedItemAttr("shipBonusORECapital4"),
                                     skill="Capital Industrial Ships")
