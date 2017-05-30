# sensorCompensationSensorStrengthBonusMagnetometric
#
# Used by:
# Skill: Magnetometric Sensor Compensation
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanMagnetometricStrength",
                           container.getModifiedItemAttr("sensorStrengthBonus") * container.level)
