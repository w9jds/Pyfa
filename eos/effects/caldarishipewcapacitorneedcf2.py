# caldariShipEwCapacitorNeedCF2
#
# Used by:
# Ship: Griffin
# Ship: Kitsune
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusCF2"), skill="Caldari Frigate")
