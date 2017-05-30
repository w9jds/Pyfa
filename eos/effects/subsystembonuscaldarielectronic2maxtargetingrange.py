# subsystemBonusCaldariElectronic2MaxTargetingRange
#
# Used by:
# Subsystem: Tengu Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("subsystemBonusCaldariElectronic2"),
                           skill="Caldari Electronic Systems")
