# subsystemBonusMinmatarPropulsionAgility
#
# Used by:
# Subsystem: Loki Propulsion - Intercalated Nanofibers
# Subsystem: Loki Propulsion - Interdiction Nullifier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("subsystemBonusMinmatarPropulsion"),
                           skill="Minmatar Propulsion Systems")
