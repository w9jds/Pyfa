# shipBonusStrategicCruiserMinmatarHeatDamage
#
# Used by:
# Ship: Loki
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  ship.getModifiedItemAttr("shipBonusStrategicCruiserMinmatar"),
                                  skill="Minmatar Strategic Cruiser")
