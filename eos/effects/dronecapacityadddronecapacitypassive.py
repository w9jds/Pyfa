# droneCapacityAdddroneCapacityPassive
#
# Used by:
# Items from category: Subsystem (42 of 80)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("droneCapacity", container.getModifiedItemAttr("droneCapacity"))
