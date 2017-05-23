# maxTargetingRangeBonusPostPercentPassive
#
# Used by:
# Modules named like: Ionic Field Projector (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties=True)
