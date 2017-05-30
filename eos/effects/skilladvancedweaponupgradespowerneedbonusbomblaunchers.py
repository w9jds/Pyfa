# skillAdvancedWeaponUpgradesPowerNeedBonusBombLaunchers
#
# Used by:
# Skill: Advanced Weapon Upgrades
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Bomb Deployment"),
                                  "power", skill.getModifiedItemAttr("powerNeedBonus") * skill.level)
