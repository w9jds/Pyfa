# modeAgilityPostDiv
#
# Used by:
# Modules named like: Propulsion Mode (4 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr(
            "agility",
            1 / container.getModifiedItemAttr("modeAgilityPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
