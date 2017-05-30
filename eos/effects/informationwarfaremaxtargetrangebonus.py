# Not used by any item
effectType = "gang"
gangBoost = "maxTargetRange"
gangBonus = "maxTargetRangeBonus"


def handler(fit, container, context):
    fit.ship.boostItemAttr(gangBoost, container.getModifiedItemAttr(gangBonus))
