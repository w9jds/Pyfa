# skillBonusSupportFightersShield
#
# Used by:
# Skill: Support Fighters
effectType = "passive"


def handler(fit, src, context):
    lvl = src.level
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Support Fighters"), "shieldCapacity",
                                   src.getModifiedItemAttr("shieldBonus") * lvl)
