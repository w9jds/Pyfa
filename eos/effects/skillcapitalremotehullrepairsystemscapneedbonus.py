# skillCapitalRemoteHullRepairSystemsCapNeedBonus
#
# Used by:
# Skill: Capital Remote Hull Repair Systems
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Hull Repair Systems"),
                                  "capacitorNeed", skill.getModifiedItemAttr("capNeedBonus") * skill.level)
