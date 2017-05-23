# shieldCommandDurationBonus
#
# Used by:
# Skill: Shield Command
effectType = "passive"


def handler(fit, src, context):
    lvl = src.level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Command"), "buffDuration",
                                  src.getModifiedItemAttr("durationBonus") * lvl)
