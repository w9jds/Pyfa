# subsystemBonusCaldariElectronic2MaxTargetingRange
#
# Used by:
# Subsystem: Tengu Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("subsystemBonusCaldariElectronic2"),
                           skill="Caldari Electronic Systems")
