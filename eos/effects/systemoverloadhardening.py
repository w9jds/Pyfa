# systemOverloadHardening
#
# Used by:
# Celestials named like: Red Giant Beacon Class (6 of 6)
runTime = "early"
effectType = ("projected", "passive")


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: "overloadHardeningBonus" in mod.itemModifiedAttributes,
                                     "overloadHardeningBonus", container.getModifiedItemAttr("overloadBonusMultiplier"))
