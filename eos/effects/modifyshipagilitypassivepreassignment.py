# modifyShipAgilityPassivePreAssignment
#
# Used by:
# Subsystems from group: Propulsion Systems (16 of 16)
runTime = "early"
effectType = "passive"


def handler(fit, container, context):
    fit.ship.preAssignItemAttr("agility", container.getModifiedItemAttr("agility"))
