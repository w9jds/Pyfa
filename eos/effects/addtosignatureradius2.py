# addToSignatureRadius2
#
# Used by:
# Modules from group: Missile Launcher Bomb (2 of 2)
# Modules from group: Shield Extender (33 of 33)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("signatureRadius", container.getModifiedItemAttr("signatureRadiusAdd"))
