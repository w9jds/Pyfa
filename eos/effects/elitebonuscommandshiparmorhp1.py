# eliteBonusCommandShipArmorHP1
#
# Used by:
# Ship: Damnation
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("eliteBonusCommandShips1"), skill="Command Ships")
