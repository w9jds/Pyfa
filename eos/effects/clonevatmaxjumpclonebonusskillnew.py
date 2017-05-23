# cloneVatMaxJumpCloneBonusSkillNew
#
# Used by:
# Skill: Cloning Facility Operation
effectType = "passive"


def handler(fit, skill, context):
    fit.ship.boostItemAttr("maxJumpClones", skill.getModifiedItemAttr("maxJumpClonesBonus") * skill.level)
