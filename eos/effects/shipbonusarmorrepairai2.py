# shipBonusArmorRepairAI2
#
# Used by:
# Ship: Impel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("shipBonusAI2"),
                                  skill="Amarr Industrial")
