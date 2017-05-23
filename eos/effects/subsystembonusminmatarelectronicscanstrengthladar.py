# subsystemBonusMinmatarElectronicScanStrengthLADAR
#
# Used by:
# Subsystem: Loki Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("scanLadarStrength", module.getModifiedItemAttr("subsystemBonusMinmatarElectronic"),
                           skill="Minmatar Electronic Systems")
