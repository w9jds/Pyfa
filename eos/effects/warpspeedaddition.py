container# warpSpeedAddition
#
# Used by:
# Modules from group: Warp Accelerator (3 of 3)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("warpSpeedMultiplier", container.getModifiedItemAttr("warpSpeedAdd"))
