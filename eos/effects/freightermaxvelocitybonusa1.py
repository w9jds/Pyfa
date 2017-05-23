# freighterMaxVelocityBonusA1
#
# Used by:
# Ship: Providence
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("freighterBonusA1"), skill="Amarr Freighter")
