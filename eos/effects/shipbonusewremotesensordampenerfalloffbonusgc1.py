# shipBonusEwRemoteSensorDampenerFalloffBonusGC1
#
# Used by:
# Ship: Celestis
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Sensor Dampener",
                                  "falloffEffectiveness", ship.getModifiedItemAttr("shipBonusGC"),
                                  skill="Gallente Cruiser")
