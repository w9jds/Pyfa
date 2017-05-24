# chargeBonusWarfareCharge
#
# Used by:
# Items from market group: Ammunition & Charges > Command Burst Charges (15 of 15)
effectType = "active"


def handler(fit, container, context):
    for x in xrange(1, 4):
        value = container.getModifiedChargeAttr("warfareBuff{}Multiplier".format(x))
        container.multiplyItemAttr("warfareBuff{}Value".format(x), value)
