# GCHYieldMultiplyPassive
#
# Used by:
# Ship: Prospect
# Ship: Venture
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Gas Cloud Harvester",
                                     "miningAmount", container.getModifiedItemAttr("miningAmountMultiplier"))
