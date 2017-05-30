# capitalLauncherSkillCruiseCitadelExplosiveDamage1
#
# Used by:
# Skill: XL Cruise Missiles
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("XL Cruise Missiles"),
                                    "explosiveDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
