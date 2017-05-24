# ammoSpeedMultiplier
#
# Used by:
# Charges from group: Festival Charges (22 of 22)
# Charges from group: Interdiction Probe (2 of 2)
# Charges from group: Survey Probe (3 of 3)
effectType = "passive"


def handler(fit, container, context):
    container.multiplyItemAttr("speed", container.getModifiedChargeAttr("speedMultiplier") or 1)
