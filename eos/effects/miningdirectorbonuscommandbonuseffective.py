# Not used by any item
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining Director"),
                                  "commandBonus", ship.getModifiedItemAttr("commandBonusEffective"))
