# overloadSelfPainterBonus
#
# Used by:
# Modules from group: Target Painter (8 of 8)
effectType = "overheat"


def handler(fit, module, context):
    module.boostItemAttr("signatureRadiusBonus", module.getModifiedItemAttr("overloadPainterStrengthBonus") or 0)
