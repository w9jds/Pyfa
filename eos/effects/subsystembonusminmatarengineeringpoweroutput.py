# subsystemBonusMinmatarEngineeringPowerOutput
#
# Used by:
# Subsystem: Loki Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("subsystemBonusMinmatarEngineering"),
                           skill="Minmatar Engineering Systems")
