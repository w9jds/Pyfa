# selfT2LargeHybridBlasterDamageBonus
#
# Used by:
# Skill: Large Blaster Specialization
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Blaster Specialization"),
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
