# skillMJDdurationBonus
#
# Used by:
# Skill: Micro Jump Drive Operation
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Micro Jump Drive Operation"),
                                  "duration", skill.getModifiedItemAttr("durationBonus") * skill.level)
