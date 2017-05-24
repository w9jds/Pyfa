# subsystemBonusCaldariDefensiveShieldHP
#
# Used by:
# Subsystem: Tengu Defensive - Supplemental Screening
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("subsystemBonusCaldariDefensive"),
                           skill="Caldari Defensive Systems")
