# subsystemBonusCaldariEngineeringPowerOutput
#
# Used by:
# Subsystem: Tengu Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("subsystemBonusCaldariEngineering"),
                           skill="Caldari Engineering Systems")
