# overloadSelfPainterBonus
#
# Used by:
# Modules from group: Target Painter (8 of 8)
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("signatureRadiusBonus", container.getModifiedItemAttr("overloadPainterStrengthBonus") or 0)
