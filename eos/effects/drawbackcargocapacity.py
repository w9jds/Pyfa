# drawbackCargoCapacity
#
# Used by:
# Modules named like: Transverse Bulkhead (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("capacity", container.getModifiedItemAttr("drawback"))
