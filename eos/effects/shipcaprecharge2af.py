# shipCapRecharge2AF
#
# Used by:
# Ship: Anathema
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("rechargeRate", ship.getModifiedItemAttr("shipBonus2AF"), skill="Amarr Frigate")
