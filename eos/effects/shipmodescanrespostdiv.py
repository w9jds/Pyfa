# Not used by any item
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr(
            "scanResolution",
            1 / container.getModifiedItemAttr("modeScanResPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
