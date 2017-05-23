# droneCapacityAdddroneCapacityPassive
#
# Used by:
# Items from category: Subsystem (42 of 80)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("droneCapacity", module.getModifiedItemAttr("droneCapacity"))
