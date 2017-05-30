# subsystemBonusAmarrElectronicScanStrengthRADAR
#
# Used by:
# Subsystem: Legion Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanRadarStrength", container.getModifiedItemAttr("subsystemBonusAmarrElectronic"),
                           skill="Amarr Electronic Systems")
