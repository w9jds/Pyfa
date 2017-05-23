# scanStrengthBonusPercentPassive
#
# Used by:
# Implants named like: High grade (20 of 66)
effectType = "passive"


def handler(fit, implant, context):
    for sensor_type in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        sensoreffectType = "scan{0}Strength".format(sensor_type)
        sensorBoost = "scan{0}StrengthPercent".format(sensor_type)
        if sensorBoost in implant.item.attributes:
            fit.ship.boostItemAttr(sensoreffectType, implant.getModifiedItemAttr(sensorBoost))
