# subsystemBonusAmarrDefensive2RemoteArmorRepairAmount
#
# Used by:
# Subsystem: Legion Defensive - Adaptive Augmenter
effectType = "passive"
runTime = "early"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"),
                                  "armorDamageAmount", container.getModifiedItemAttr("subsystemBonusAmarrDefensive2"),
                                  skill="Amarr Defensive Systems")
