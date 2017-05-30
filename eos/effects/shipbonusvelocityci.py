# shipBonusVelocityCI
#
# Used by:
# Variations of ship: Tayra (2 of 2)
# Ship: Crane
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusCI"), skill="Caldari Industrial")
