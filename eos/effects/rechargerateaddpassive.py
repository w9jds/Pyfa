# rechargeRateAddPassive
#
# Used by:
# Subsystems from group: Engineering Systems (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("rechargeRate", container.getModifiedItemAttr("rechargeRate"))
