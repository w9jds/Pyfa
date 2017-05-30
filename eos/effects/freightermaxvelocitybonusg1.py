# freighterMaxVelocityBonusG1
#
# Used by:
# Ship: Obelisk
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("freighterBonusG1"), skill="Gallente Freighter")
