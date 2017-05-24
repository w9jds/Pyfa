# subsystemBonusAmarrPropulsionAgility
#
# Used by:
# Subsystem: Legion Propulsion - Interdiction Nullifier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("subsystemBonusAmarrPropulsion"),
                           skill="Amarr Propulsion Systems")
