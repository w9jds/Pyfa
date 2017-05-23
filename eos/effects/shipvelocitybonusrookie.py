# shipVelocityBonusRookie
#
# Used by:
# Ship: Reaper
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("rookieShipVelocityBonus"))
