# signatureRadiusPreAssignment
#
# Used by:
# Subsystems from group: Defensive Systems (16 of 16)
effectType = "passive"
runTime = "early"


def handler(fit, module, context):
    fit.ship.preAssignItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadius"))
