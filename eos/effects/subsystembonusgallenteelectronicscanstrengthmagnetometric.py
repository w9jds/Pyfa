# subsystemBonusGallenteElectronicScanStrengthMagnetometric
#
# Used by:
# Subsystem: Proteus Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanMagnetometricStrength", container.getModifiedItemAttr("subsystemBonusGallenteElectronic"),
                           skill="Gallente Electronic Systems")
