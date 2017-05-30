# subsystemBonusAmarrDefensiveArmorRepairAmount
#
# Used by:
# Subsystem: Legion Defensive - Nanobot Injector
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", container.getModifiedItemAttr("subsystemBonusAmarrDefensive"),
                                  skill="Amarr Defensive Systems")
