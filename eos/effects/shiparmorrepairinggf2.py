# shipArmorRepairingGF2
#
# Used by:
# Ship: Incursus
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("shipBonusGF2"),
                                  skill="Gallente Frigate")
