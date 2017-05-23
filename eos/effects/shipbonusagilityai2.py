# shipBonusAgilityAI2
#
# Used by:
# Ship: Sigil
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("shipBonusAI2"), skill="Amarr Industrial")
