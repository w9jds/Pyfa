# ewSkillRsdFallOffBonus
#
# Used by:
# Skill: Frequency Modulation
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Sensor Linking"),
                                  "falloffEffectiveness", skill.getModifiedItemAttr("falloffBonus") * skill.level)
