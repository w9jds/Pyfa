# subsystemBonusWarpBubbleImmune
#
# Used by:
# Subsystems named like: Propulsion Interdiction Nullifier (4 of 4)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.forceItemAttr("warpBubbleImmune", module.getModifiedItemAttr("warpBubbleImmuneModifier"))
