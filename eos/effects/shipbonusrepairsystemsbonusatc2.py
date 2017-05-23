# shipBonusRepairSystemsBonusATC2
#
# Used by:
# Ship: Vangel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("shipBonusATC2"))
