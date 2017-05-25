# Not used by any item
effectType = "passive"
runTime = "late"


def handler(fit, container, context):
    for x in xrange(1, 4):
        container.boostChargeAttr("warfareBuff{}Multiplier".format(x), container.getModifiedItemAttr("commandBurstStrengthBonus"))
