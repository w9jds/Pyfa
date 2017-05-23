# subsystemBonusCaldariElectronicScanStrengthGravimetric
#
# Used by:
# Subsystem: Tengu Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("scanGravimetricStrength", module.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                           skill="Caldari Electronic Systems")
