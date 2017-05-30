# modifyMaxVelocityOfShipPassive
#
# Used by:
# Modules from group: Expanded Cargohold (7 of 7)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("maxVelocity", container.getModifiedItemAttr("maxVelocityModifier"), stackingPenalties=True)
