# fuelConservationCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringAfterburner
#
# Used by:
# Skill: Afterburner
# Skill: Fuel Conservation
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "capacitorNeed", skill.getModifiedItemAttr("capNeedBonus") * skill.level)
