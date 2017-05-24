# systemShieldRepairAmountShieldSkills
#
# Used by:
# Celestials named like: Cataclysmic Variable Effect Beacon Class (6 of 6)
runTime = "early"
effectType = ("projected", "passive")


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Shield Operation") or
                                                 mod.item.requiresSkill("Capital Shield Operation"),
                                     "shieldBonus", container.getModifiedItemAttr("shieldBonusMultiplier"),
                                     stackingPenalties=True, penaltyGroup="postMul")
