# scanResolutionAddPassive
#
# Used by:
# Subsystems from group: Electronic Systems (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("scanResolution", container.getModifiedItemAttr("scanResolution"))
