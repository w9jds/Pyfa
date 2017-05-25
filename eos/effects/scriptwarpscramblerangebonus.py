# scriptWarpScrambleRangeBonus
#
# Used by:
# Charges from group: Warp Disruption Script (2 of 2)
effectType = "passive"


def handler(fit, container, context):
    container.boostItemAttr("warpScrambleRange", container.getModifiedChargeAttr("warpScrambleRangeBonus"))
