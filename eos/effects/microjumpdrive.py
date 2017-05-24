# microJumpDrive
#
# Used by:
# Modules from group: Micro Jump Drive (2 of 2)
effectType = "active"


def handler(fit, container, context):
    fit.ship.boostItemAttr("signatureRadius", container.getModifiedItemAttr("signatureRadiusBonusPercent"))
