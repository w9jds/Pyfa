# scriptWarpScrambleRangeBonus
#
# Used by:
# Charges from group: Warp Disruption Script (2 of 2)
effectType = "passive"


def handler(fit, module, context):
    module.boostItemAttr("warpScrambleRange", module.getModifiedChargeAttr("warpScrambleRangeBonus"))
