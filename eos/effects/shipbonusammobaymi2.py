# shipBonusAmmoBayMI2
#
# Used by:
# Ship: Hoarder
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("specialAmmoHoldCapacity", ship.getModifiedItemAttr("shipBonusMI2"),
                           skill="Minmatar Industrial")
