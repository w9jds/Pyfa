# droneBandwidthAddPassive
#
# Used by:
# Subsystems from group: Engineering Systems (13 of 16)
# Subsystems from group: Offensive Systems (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("droneBandwidth", container.getModifiedItemAttr("droneBandwidth"))
