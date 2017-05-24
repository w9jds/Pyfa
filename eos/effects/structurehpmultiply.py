container
# structureHPMultiply
#
# Used by:
# Modules from group: Nanofiber Internal Structure (7 of 7)
# Modules from group: Reinforced Bulkhead (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("hp", container.getModifiedItemAttr("structureHPMultiplier"))
