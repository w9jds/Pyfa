# sensorCompensationSensorStrengthBonusRadar
#
# Used by:
# Skill: Radar Sensor Compensation
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanRadarStrength", container.getModifiedItemAttr("sensorStrengthBonus") * container.level)
