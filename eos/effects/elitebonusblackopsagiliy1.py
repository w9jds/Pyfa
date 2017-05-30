# eliteBonusBlackOpsAgiliy1
#
# Used by:
# Ship: Sin
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("eliteBonusBlackOps1"), skill="Black Ops")
