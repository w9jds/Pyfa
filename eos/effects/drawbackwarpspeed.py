# drawbackWarpSpeed
#
# Used by:
# Modules from group: Rig Anchor (4 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("warpSpeedMultiplier", container.getModifiedItemAttr("drawback"), stackingPenalties=True)
