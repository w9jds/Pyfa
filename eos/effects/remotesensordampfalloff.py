# remoteSensorDampFalloff
#
# Used by:
# Modules from group: Sensor Dampener (6 of 6)
effectType = "projected", "active"


def handler(fit, container, context, *args, **kwargs):
    if "projected" not in context:
        return

    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties=True, *args, **kwargs)

    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties=True, *args, **kwargs)
