# emShieldCompensationHardeningBonusGroupShieldAmp
#
# Used by:
# Skill: EM Shield Compensation
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Resistance Amplifier",
                                  "emDamageResistanceBonus", skill.getModifiedItemAttr("hardeningBonus") * skill.level)
