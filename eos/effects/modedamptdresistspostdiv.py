# modeDampTDResistsPostDiv
#
# Used by:
# Modules named like: Sharpshooter Mode (4 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("weaponDisruptionResistance", 1 / container.getModifiedItemAttr("modeEwarResistancePostDiv"))
    fit.ship.multiplyItemAttr("sensorDampenerResistance", 1 / container.getModifiedItemAttr("modeEwarResistancePostDiv"))
