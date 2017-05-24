# signatureRadiusPreAssignment
#
# Used by:
# Subsystems from group: Defensive Systems (16 of 16)
effectType = "passive"
runTime = "early"


def handler(fit, container, context):
    fit.ship.preAssignItemAttr("signatureRadius", container.getModifiedItemAttr("signatureRadius"))
