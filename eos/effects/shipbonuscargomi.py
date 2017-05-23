# shipBonusCargoMI
#
# Used by:
# Variations of ship: Wreathe (2 of 2)
# Ship: Mammoth
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusMI"), skill="Minmatar Industrial")
