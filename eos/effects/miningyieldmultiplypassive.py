# miningYieldMultiplyPassive
#
# Used by:
# Variations of ship: Venture (3 of 3)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Mining"),
                                     "miningAmount", container.getModifiedItemAttr("miningAmountMultiplier"))
