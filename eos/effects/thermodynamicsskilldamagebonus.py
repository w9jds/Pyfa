# thermodynamicsSkillDamageBonus
#
# Used by:
# Skill: Thermodynamics
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  skill.getModifiedItemAttr("thermodynamicsHeatDamage") * skill.level)
