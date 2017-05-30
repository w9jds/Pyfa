# freighterAgilityBonus2O2
#
# Used by:
# Ship: Bowhead
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("shipMaintenanceBayCapacity", ship.getModifiedItemAttr("freighterBonusO1"),
                           skill="ORE Freighter")
