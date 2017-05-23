# shipArmorRepairingRookie
#
# Used by:
# Ship: Velator
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("rookieArmorRepBonus"))
