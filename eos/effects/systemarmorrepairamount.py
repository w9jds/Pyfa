# systemArmorRepairAmount
#
# Used by:
# Celestials named like: Cataclysmic Variable Effect Beacon Class (6 of 6)
runTime = "early"
effectType = ("projected", "passive")


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Repair Systems") or
                                                 mod.item.requiresSkill("Capital Repair Systems"),
                                     "armorDamageAmount", container.getModifiedItemAttr("armorDamageAmountMultiplier"),
                                     stackingPenalties=True, penaltyGroup="postMul")
