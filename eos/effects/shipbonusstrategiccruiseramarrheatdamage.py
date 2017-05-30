# shipBonusStrategicCruiserAmarrHeatDamage
#
# Used by:
# Ship: Legion
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  ship.getModifiedItemAttr("shipBonusStrategicCruiserAmarr"),
                                  skill="Amarr Strategic Cruiser")
