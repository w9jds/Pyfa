# selfT2LargeProjectileArtyDamageBonus
#
# Used by:
# Skill: Large Artillery Specialization
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Artillery Specialization"),
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
