# subsystemBonusGallenteDefensive2RemoteArmorRepairAmount
#
# Used by:
# Subsystem: Proteus Defensive - Adaptive Augmenter
effectType = "passive"
runTime = "early"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"),
                                  "armorDamageAmount", container.getModifiedItemAttr("subsystemBonusGallenteDefensive2"),
                                  skill="Gallente Defensive Systems")
