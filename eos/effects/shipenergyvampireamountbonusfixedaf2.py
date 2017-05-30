# shipEnergyVampireAmountBonusFixedAF2
#
# Used by:
# Ship: Malice
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Nosferatu",
                                  "powerTransferAmount", ship.getModifiedItemAttr("shipBonus2AF"),
                                  skill="Amarr Frigate")
