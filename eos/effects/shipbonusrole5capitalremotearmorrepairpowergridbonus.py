# shipBonusRole5CapitalRemoteArmorRepairPowergridBonus
#
# Used by:
# Ship: Dagon
effectType = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Armor Repair Systems"), "power", src.getModifiedItemAttr("shipBonusRole5"))
