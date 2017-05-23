# shipBonusRemoteRepairAmountPirateFaction
#
# Used by:
# Ship: Nestor
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("shipBonusRole7"))
