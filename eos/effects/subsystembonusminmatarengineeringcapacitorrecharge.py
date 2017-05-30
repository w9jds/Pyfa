# subsystemBonusMinmatarEngineeringCapacitorRecharge
#
# Used by:
# Subsystem: Loki Engineering - Capacitor Regeneration Matrix
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("rechargeRate", container.getModifiedItemAttr("subsystemBonusMinmatarEngineering"),
                           skill="Minmatar Engineering Systems")
