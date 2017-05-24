# miningInfoMultiplier
#
# Used by:
# Charges from group: Mining Crystal (30 of 30)
# Charges named like: Mining Crystal (32 of 32)
effectType = "passive"


def handler(fit, container, context):
    container.multiplyItemAttr("specialtyMiningAmount",
                               container.getModifiedChargeAttr("specialisationAsteroidYieldMultiplier"))
    # module.multiplyItemAttr("miningAmount", module.getModifiedChargeAttr("specialisationAsteroidYieldMultiplier"))
