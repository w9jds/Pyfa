# missileSkillWarheadUpgradesKineticDamageBonus
#
# Used by:
# Skill: Warhead Upgrades
effectType = "passive"


def handler(fit, skill, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "kineticDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
