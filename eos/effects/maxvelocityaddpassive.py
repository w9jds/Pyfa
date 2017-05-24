# maxVelocityAddPassive
#
# Used by:
# Subsystems from group: Propulsion Systems (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("maxVelocity", container.getModifiedItemAttr("maxVelocity"))
