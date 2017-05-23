# eliteBonusBlackOpsECMBurstGravAndLadarAndMagnetoAndRadar
#
# Used by:
# Ship: Widow
effectType = "passive"


def handler(fit, ship, context):
    sensorTypes = ("Gravimetric", "Ladar", "Magnetometric", "Radar")
    for sensor_type in sensorTypes:
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Burst Jammer",
                                      "scan{0}StrengthBonus".format(sensor_type),
                                      ship.getModifiedItemAttr("eliteBonusBlackOps1"), skill="Black Ops")
