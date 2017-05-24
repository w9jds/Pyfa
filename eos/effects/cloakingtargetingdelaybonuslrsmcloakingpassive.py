# cloakingTargetingDelayBonusLRSMCloakingPassive
#
# Used by:
# Modules named like: Targeting Systems Stabilizer (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda container: container.item.requiresSkill("Cloaking"),
                                  "cloakingTargetingDelay", container.getModifiedItemAttr("cloakingTargetingDelayBonus"))
