# shipBonusEwRemoteSensorDampenerScanResolutionBonusRookie
#
# Used by:
# Ship: Velator
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Sensor Dampener",
                                  "scanResolutionBonus", ship.getModifiedItemAttr("rookieDampStrengthBonus"))
