# warpScramble
#
# Used by:
# Modules named like: Warp Disruptor (27 of 27)
effectType = "projected", "active"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))
