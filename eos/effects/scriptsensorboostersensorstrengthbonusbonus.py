
# scriptSensorBoosterSensorStrengthBonusBonus
#
# Used by:
# Charges from group: Sensor Booster Script (3 of 3)
effectType = "active"


def handler(fit, container, context):
    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        container.boostItemAttr("scan{}StrengthPercent".format(scanType),
                                container.getModifiedChargeAttr("sensorStrengthBonusBonus"))
