# subsystemBonusCaldariElectronicScanStrengthGravimetric
#
# Used by:
# Subsystem: Tengu Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanGravimetricStrength", container.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                           skill="Caldari Electronic Systems")
