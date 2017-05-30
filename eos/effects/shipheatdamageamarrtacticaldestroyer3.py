# shipHeatDamageAmarrTacticalDestroyer3
#
# Used by:
# Ship: Confessor
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  ship.getModifiedItemAttr("shipBonusTacticalDestroyerAmarr3"),
                                  skill="Amarr Tactical Destroyer")
