# warpSpeedAddition
#
# Used by:
# Modules from group: Warp Accelerator (3 of 3)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("warpSpeedMultiplier", module.getModifiedItemAttr("warpSpeedAdd"))
