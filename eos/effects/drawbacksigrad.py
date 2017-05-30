# drawbackSigRad
#
# Used by:
# Modules from group: Rig Shield (72 of 72)
# Modules named like: Optimizer (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("signatureRadius", container.getModifiedItemAttr("drawback"), stackingPenalties=True)
