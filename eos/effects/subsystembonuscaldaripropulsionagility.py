# subsystemBonusCaldariPropulsionAgility
#
# Used by:
# Subsystem: Tengu Propulsion - Intercalated Nanofibers
# Subsystem: Tengu Propulsion - Interdiction Nullifier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("subsystemBonusCaldariPropulsion"),
                           skill="Caldari Propulsion Systems")
