# skillMultiplierDefenderMissileVelocity
#
# Used by:
# Skill: Defender Missiles
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Defender Missiles"),
                                    "maxVelocity", skill.getModifiedItemAttr("missileVelocityBonus") * skill.level)
