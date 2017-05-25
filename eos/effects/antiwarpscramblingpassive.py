# antiWarpScramblingPassive
#
# Used by:
# Modules from group: Warp Core Stabilizer (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("warmScrambleStatus", container.getModifiedItemAttr("warpScrambleStrength"))
