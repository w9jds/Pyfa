# remoteSensorBoostFalloff
#
# Used by:
# Modules from group: Remote Sensor Booster (8 of 8)
effectType = "projected", "active"


def handler(fit, container, context):
    if "projected" not in context:
        return

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
