# drawbackCargoCapacity
#
# Used by:
# Modules named like: Transverse Bulkhead (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("capacity", module.getModifiedItemAttr("drawback"))
