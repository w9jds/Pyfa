# subsystemBonusGallenteElectronic2MaxTargetingRange
#
# Used by:
# Subsystem: Proteus Electronics - Dissolution Sequencer
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("subsystemBonusGallenteElectronic2"),
                           skill="Gallente Electronic Systems")
