# jumpDriveSkillsRangeBonus
#
# Used by:
# Skill: Jump Drive Calibration
effectType = "passive"


def handler(fit, skill, context):
    fit.ship.boostItemAttr("jumpDriveRange", skill.getModifiedItemAttr("jumpDriveRangeBonus") * skill.level)
