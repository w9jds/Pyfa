# skillBonusLightFighters
#
# Used by:
# Skill: Light Fighters
effectType = "passive"


def handler(fit, src, context):
    lvl = src.level
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Light Fighters"), "maxVelocity",
                                   src.getModifiedItemAttr("maxVelocityBonus") * lvl)
