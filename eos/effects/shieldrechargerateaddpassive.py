# shieldRechargeRateAddPassive
#
# Used by:
# Subsystems from group: Defensive Systems (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("shieldRechargeRate", container.getModifiedItemAttr("shieldRechargeRate") or 0)
