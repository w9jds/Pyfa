# skillTriageModuleConsumptionQuantityBonus
#
# Used by:
# Skill: Tactical Logistics Reconfiguration
effectType = "passive"


def handler(fit, skill, context):
    amount = -skill.getModifiedItemAttr("consumptionQuantityBonus")
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill(skill),
                                     "consumptionQuantity", amount * skill.level)
