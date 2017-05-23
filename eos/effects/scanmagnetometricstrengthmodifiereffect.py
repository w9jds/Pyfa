# ScanMagnetometricStrengthModifierEffect
#
# Used by:
# Implants named like: Low grade Spur (5 of 6)
effectType = "passive"


def handler(fit, implant, context):
    fit.ship.increaseItemAttr("scanMagnetometricStrength",
                              implant.getModifiedItemAttr("scanMagnetometricStrengthModifier"))
