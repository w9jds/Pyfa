# shipBonusHeatDamageATF1
#
# Used by:
# Ship: Cambion
# Ship: Etana
# Ship: Utu
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  ship.getModifiedItemAttr("shipBonusATF1"))
