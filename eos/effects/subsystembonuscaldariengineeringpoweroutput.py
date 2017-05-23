# subsystemBonusCaldariEngineeringPowerOutput
#
# Used by:
# Subsystem: Tengu Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("subsystemBonusCaldariEngineering"),
                           skill="Caldari Engineering Systems")
