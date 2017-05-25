# sensorBoosterActivePercentage
#
# Used by:
# Modules from group: Sensor Booster (16 of 16)
effectType = "active"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties=True)
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties=True)

    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.boostItemAttr(
                "scan{}Strength".format(scanType),
                container.getModifiedItemAttr("scan{}StrengthPercent".format(scanType)),
                stackingPenalties=True
        )
