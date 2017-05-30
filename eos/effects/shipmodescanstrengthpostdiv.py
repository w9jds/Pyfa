# shipModeScanStrengthPostDiv
#
# Used by:
# Modules named like: Sharpshooter Mode (4 of 4)
effectType = "passive"


def handler(fit, container, context):
    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.multiplyItemAttr(
                "scan{}Strength".format(scanType),
                1 / (container.getModifiedItemAttr("mode{}StrengthPostDiv".format(scanType)) or 1),
                stackingPenalties=True,
                penaltyGroup="postDiv"
        )
