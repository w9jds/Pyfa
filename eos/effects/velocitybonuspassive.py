# velocityBonusPassive
#
# Used by:
# Modules named like: Polycarbon Engine Housing (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("implantBonusVelocity"),
                           stackingPenalties=True)
