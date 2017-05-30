# cargoCapacityMultiply
#
# Used by:
# Modules from group: Expanded Cargohold (7 of 7)
# Modules from group: Overdrive Injector System (7 of 7)
# Modules from group: Reinforced Bulkhead (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("capacity", container.getModifiedItemAttr("cargoCapacityMultiplier"))
