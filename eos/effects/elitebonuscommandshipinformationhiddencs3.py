# Not used by any item
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Information Command Specialist"),
                                  "commandBonusHidden", module.getModifiedItemAttr("eliteBonusCommandShips3"), skill="Command Ships")
