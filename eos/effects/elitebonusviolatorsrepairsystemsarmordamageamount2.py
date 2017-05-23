# eliteBonusViolatorsRepairSystemsArmorDamageAmount2
#
# Used by:
# Ship: Kronos
# Ship: Paladin
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("eliteBonusViolators2"),
                                  skill="Marauders")
