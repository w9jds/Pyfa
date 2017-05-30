# modeVelocityPostDiv
#
# Used by:
# Module: Jackdaw Propulsion Mode
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr(
            "maxVelocity",
            1 / container.getModifiedItemAttr("modeVelocityPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
