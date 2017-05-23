# Not used by any item
effectType = "passive"


def handler(fit, ship, context):
    if fit.extraAttributes["siege"]:
        fit.ship.increaseItemAttr("commandBonusEffective", ship.getModifiedItemAttr("shipBonusORECapital2"),
                                  skill="Capital Industrial Ships")
