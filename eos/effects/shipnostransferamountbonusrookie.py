# shipNOSTransferAmountBonusRookie
#
# Used by:
# Ship: Hematos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Nosferatu",
                                  "powerTransferAmount", ship.getModifiedItemAttr("rookieNosDrain"))
