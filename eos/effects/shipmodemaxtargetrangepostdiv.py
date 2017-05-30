# shipModeMaxTargetRangePostDiv
#
# Used by:
# Modules named like: Sharpshooter Mode (4 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr(
            "maxTargetRange",
            1 / container.getModifiedItemAttr("modeMaxTargetRangePostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
