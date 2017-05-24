# subsystemBonusAmarrElectronic2MaxTargetingRange
#
# Used by:
# Subsystem: Legion Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("subsystemBonusAmarrElectronic2"),
                           skill="Amarr Electronic Systems")
