# subsystemBonusGallentePropulsionAgility
#
# Used by:
# Subsystem: Proteus Propulsion - Interdiction Nullifier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("subsystemBonusGallentePropulsion"),
                           skill="Gallente Propulsion Systems")
