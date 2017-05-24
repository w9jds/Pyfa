# subsystemBonusCaldariEngineeringCapacitorRecharge
#
# Used by:
# Subsystem: Tengu Engineering - Capacitor Regeneration Matrix
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("rechargeRate", container.getModifiedItemAttr("subsystemBonusCaldariEngineering"),
                           skill="Caldari Engineering Systems")
