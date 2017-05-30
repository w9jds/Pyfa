# shipBonusRole1CommandBurstCPUBonus
#
# Used by:
# Ships from group: Force Auxiliary (5 of 5)
effectType = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Leadership"), "cpu",
                                  src.getModifiedItemAttr("shipBonusRole1"))
