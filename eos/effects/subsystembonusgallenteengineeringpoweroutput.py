# subsystemBonusGallenteEngineeringPowerOutput
#
# Used by:
# Subsystem: Proteus Engineering - Power Core Multiplier
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("subsystemBonusGallenteEngineering"),
                           skill="Gallente Engineering Systems")
