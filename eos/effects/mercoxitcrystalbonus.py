# mercoxitCrystalBonus
#
# Used by:
# Module: Medium Mercoxit Mining Crystal Optimization I
effectType = "passive"
runTime = "early"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Mercoxit Processing"),
                                    "specialisationAsteroidYieldMultiplier",
                                    container.getModifiedItemAttr("miningAmountBonus"))
