# shipBonusPICommoditiesHoldGI2
#
# Used by:
# Ship: Epithal
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("specialPlanetaryCommoditiesHoldCapacity", ship.getModifiedItemAttr("shipBonusGI2"),
                           skill="Gallente Industrial")
