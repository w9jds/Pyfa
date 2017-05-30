# subsystemBonusAmarrEngineeringPowerOutput
#
# Used by:
# Subsystem: Legion Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("subsystemBonusAmarrEngineering"),
                           skill="Amarr Engineering Systems")
