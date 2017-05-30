# freighterAgilityBonusG1
#
# Used by:
# Ship: Anshar
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("freighterBonusG1"), skill="Gallente Freighter")
