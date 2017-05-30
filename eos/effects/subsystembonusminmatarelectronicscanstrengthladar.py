# subsystemBonusMinmatarElectronicScanStrengthLADAR
#
# Used by:
# Subsystem: Loki Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanLadarStrength", container.getModifiedItemAttr("subsystemBonusMinmatarElectronic"),
                           skill="Minmatar Electronic Systems")
