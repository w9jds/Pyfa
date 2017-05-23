# shipEnergyTransferRange2
#
# Used by:
# Ship: Basilisk
# Ship: Etana
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Capacitor Transmitter",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusCC2"), skill="Caldari Cruiser")
