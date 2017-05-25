# capacitorCapacityAddPassive
#
# Used by:
# Subsystems from group: Engineering Systems (16 of 16)
# Subsystem: Tengu Offensive - Magnetic Infusion Basin
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("capacitorCapacity",
                              container.getModifiedItemAttr("capacitorCapacity"))
