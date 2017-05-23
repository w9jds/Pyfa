# explosiveArmorCompensationHardeningBonusGroupEnergized
#
# Used by:
# Skill: Explosive Armor Compensation
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Plating Energized",
                                  "explosiveDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningBonus") * skill.level)
