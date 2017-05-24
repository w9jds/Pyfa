# subsystemBonusMinmatarElectronic2MaxTargetingRange
#
# Used by:
# Subsystem: Loki Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("subsystemBonusMinmatarElectronic2"),
                           skill="Minmatar Electronic Systems")
