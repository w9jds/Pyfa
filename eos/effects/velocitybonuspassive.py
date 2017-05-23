# velocityBonusPassive
#
# Used by:
# Modules named like: Polycarbon Engine Housing (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("implantBonusVelocity"),
                           stackingPenalties=True)
