# subsystemBonusGallenteEngineeringPowerOutput
#
# Used by:
# Subsystem: Proteus Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("subsystemBonusGallenteEngineering"),
                           skill="Gallente Engineering Systems")
