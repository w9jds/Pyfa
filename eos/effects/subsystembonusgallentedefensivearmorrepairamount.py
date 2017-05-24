# subsystemBonusGallenteDefensiveArmorRepairAmount
#
# Used by:
# Subsystem: Proteus Defensive - Nanobot Injector
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", container.getModifiedItemAttr("subsystemBonusGallenteDefensive"),
                                  skill="Gallente Defensive Systems")
