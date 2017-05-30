# shipBonusStrategicCruiserCaldariHeatDamage
#
# Used by:
# Ship: Tengu
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  ship.getModifiedItemAttr("shipBonusStrategicCruiserCaldari"),
                                  skill="Caldari Strategic Cruiser")
