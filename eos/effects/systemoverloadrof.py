# systemOverloadRof
#
# Used by:
# Celestials named like: Red Giant Beacon Class (6 of 6)
runTime = "early"
effectType = ("projected", "passive")


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: "overloadRofBonus" in mod.itemModifiedAttributes,
                                     "overloadRofBonus", container.getModifiedItemAttr("overloadBonusMultiplier"))
