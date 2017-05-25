# Not used by any item
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Information Command Specialist"),
                                  "commandBonusHidden", container.getModifiedItemAttr("eliteBonusCommandShips3"), skill="Command Ships")
