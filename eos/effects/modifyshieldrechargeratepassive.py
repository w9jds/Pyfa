# modifyShieldRechargeRatePassive
#
# Used by:
# Modules named like: Processor Overclocking Unit (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.multiplyItemAttr("shieldRechargeRate", module.getModifiedItemAttr("shieldRechargeRateMultiplier"))
