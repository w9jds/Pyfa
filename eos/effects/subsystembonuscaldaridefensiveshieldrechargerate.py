# subsystemBonusCaldariDefensiveShieldRechargeRate
#
# Used by:
# Subsystem: Tengu Defensive - Supplemental Screening
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("shieldRechargeRate", container.getModifiedItemAttr("subsystemBonusCaldariDefensive2"),
                           skill="Caldari Defensive Systems")
