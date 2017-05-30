# freighterAgilityBonusA1
#
# Used by:
# Ship: Ark
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("freighterBonusA1"), skill="Amarr Freighter")
