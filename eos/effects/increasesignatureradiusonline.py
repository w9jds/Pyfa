# increaseSignatureRadiusOnline
#
# Used by:
# Modules from group: Inertial Stabilizer (7 of 7)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("signatureRadius", container.getModifiedItemAttr("signatureRadiusBonus"))
