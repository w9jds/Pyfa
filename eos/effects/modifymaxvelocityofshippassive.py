# modifyMaxVelocityOfShipPassive
#
# Used by:
# Modules from group: Expanded Cargohold (7 of 7)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedItemAttr("maxVelocityModifier"), stackingPenalties=True)
