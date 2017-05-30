# cloakingTargetingDelayBonusPostPercentCloakingTargetingDelayBonusForShipModulesRequiringCloaking
#
# Used by:
# Skill: Cloaking
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Cloaking"),
                                  "cloakingTargetingDelay",
                                  skill.getModifiedItemAttr("cloakingTargetingDelayBonus") * skill.level)
