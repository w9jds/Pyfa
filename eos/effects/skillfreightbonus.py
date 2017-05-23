# skillFreightBonus
#
# Used by:
# Modules named like: Cargohold Optimization (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("capacity", module.getModifiedItemAttr("cargoCapacityBonus"))
