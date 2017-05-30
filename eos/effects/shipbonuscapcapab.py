# shipBonusCapCapAB
#
# Used by:
# Ship: Apocalypse Imperial Issue
# Ship: Paladin
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("capacitorCapacity", ship.getModifiedItemAttr("shipBonusAB2"), skill="Amarr Battleship")
