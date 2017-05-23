# scanResolutionAddPassive
#
# Used by:
# Subsystems from group: Electronic Systems (16 of 16)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("scanResolution", module.getModifiedItemAttr("scanResolution"))
