# modeSigRadiusPostDiv
#
# Used by:
# Module: Confessor Defense Mode
# Module: Jackdaw Defense Mode
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("signatureRadius", 1 / container.getModifiedItemAttr("modeSignatureRadiusPostDiv"),
                              stackingPenalties=True, penaltyGroup="postDiv")
