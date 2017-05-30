# skillCapitalShipsAdvancedAgility
#
# Used by:
# Skill: Capital Ships
effectType = "passive"


def handler(fit, skill, context):
    if fit.ship.item.requiresSkill("Capital Ships"):
        fit.ship.boostItemAttr("agility", skill.getModifiedItemAttr("agilityBonus") * skill.level)
