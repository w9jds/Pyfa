# eliteBonusBlackOpsMaxVelocity1
#
# Used by:
# Ship: Panther
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("eliteBonusBlackOps1"), skill="Black Ops")
