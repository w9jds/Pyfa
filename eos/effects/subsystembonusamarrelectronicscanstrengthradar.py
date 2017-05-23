# subsystemBonusAmarrElectronicScanStrengthRADAR
#
# Used by:
# Subsystem: Legion Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("scanRadarStrength", module.getModifiedItemAttr("subsystemBonusAmarrElectronic"),
                           skill="Amarr Electronic Systems")
