# modifyShieldRechargeRatePassive
#
# Used by:
# Modules named like: Processor Overclocking Unit (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("shieldRechargeRate", container.getModifiedItemAttr("shieldRechargeRateMultiplier"))
