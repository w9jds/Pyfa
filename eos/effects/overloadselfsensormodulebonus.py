# overloadSelfSensorModuleBonus
#
# Used by:
# Modules from group: Remote Sensor Booster (8 of 8)
# Modules from group: Sensor Booster (16 of 16)
# Modules from group: Sensor Dampener (6 of 6)
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("maxTargetRangeBonus", container.getModifiedItemAttr("overloadSensorModuleStrengthBonus"))
    container.boostItemAttr("scanResolutionBonus", container.getModifiedItemAttr("overloadSensorModuleStrengthBonus"),
                            stackingPenalties=True)

    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        container.boostItemAttr(
                "scan{}StrengthPercent".format(scanType),
                container.getModifiedItemAttr("overloadSensorModuleStrengthBonus"),
                stackingPenalties=True
        )
