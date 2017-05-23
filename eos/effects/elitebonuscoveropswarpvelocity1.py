# eliteBonusCoverOpsWarpVelocity1
#
# Used by:
# Ship: Pacifier
effectType = "passive"


def handler(fit, src, context):
    fit.ship.boostItemAttr("warpSpeedMultiplier", src.getModifiedItemAttr("eliteBonusCoverOps1"), skill="Covert Ops")
