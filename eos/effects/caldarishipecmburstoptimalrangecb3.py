# caldariShipECMBurstOptimalRangeCB3
#
# Used by:
# Ship: Scorpion
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Burst Jammer",
                                  "ecmBurstRange", ship.getModifiedItemAttr("shipBonusCB3"), skill="Caldari Battleship")
