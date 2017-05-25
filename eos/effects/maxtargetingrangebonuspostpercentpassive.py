# maxTargetingRangeBonusPostPercentPassive
#
# Used by:
# Modules named like: Ionic Field Projector (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties=True)
