# subsystemBonusAmarrEngineeringCapacitorRecharge
#
# Used by:
# Subsystem: Legion Engineering - Capacitor Regeneration Matrix
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("rechargeRate", container.getModifiedItemAttr("subsystemBonusAmarrEngineering"),
                           skill="Amarr Engineering Systems")
