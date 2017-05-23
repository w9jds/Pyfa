# sensorCompensationSensorStrengthBonusLadar
#
# Used by:
# Skill: Ladar Sensor Compensation
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanLadarStrength", container.getModifiedItemAttr("sensorStrengthBonus") * container.level)
