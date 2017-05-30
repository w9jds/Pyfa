# scanStrengthBonusPercentOnline
#
# Used by:
# Modules from group: Signal Amplifier (7 of 7)
effectType = "passive"


def handler(fit, container, context):
    for sensor_type in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.boostItemAttr("scan%sStrength" % sensor_type,
                               container.getModifiedItemAttr("scan%sStrengthPercent" % sensor_type),
                               stackingPenalties=True)
