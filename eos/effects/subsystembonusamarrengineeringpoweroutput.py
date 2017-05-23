# subsystemBonusAmarrEngineeringPowerOutput
#
# Used by:
# Subsystem: Legion Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("subsystemBonusAmarrEngineering"),
                           skill="Amarr Engineering Systems")
