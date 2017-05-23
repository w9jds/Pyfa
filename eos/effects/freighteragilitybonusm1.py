# freighterAgilityBonusM1
#
# Used by:
# Ship: Nomad
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("freighterBonusM1"), skill="Minmatar Freighter")
