# scriptWarpDisruptionFieldGeneratorSetDisallowInEmpireSpace
#
# Used by:
# Charges from group: Warp Disruption Script (2 of 2)
effectType = "passive"


def handler(fit, container, context):
    container.forceItemAttr("disallowInEmpireSpace", container.getModifiedChargeAttr("disallowInEmpireSpace"))
