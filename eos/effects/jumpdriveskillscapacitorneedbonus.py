# jumpDriveSkillsCapacitorNeedBonus
#
# Used by:
# Skill: Jump Drive Operation
effectType = "passive"


def handler(fit, skill, context):
    fit.ship.boostItemAttr("jumpDriveCapacitorNeed",
                           skill.getModifiedItemAttr("jumpDriveCapacitorNeedBonus") * skill.level)
