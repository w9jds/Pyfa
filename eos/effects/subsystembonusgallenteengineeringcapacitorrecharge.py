# subsystemBonusGallenteEngineeringCapacitorRecharge
#
# Used by:
# Subsystem: Proteus Engineering - Capacitor Regeneration Matrix
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("rechargeRate", container.getModifiedItemAttr("subsystemBonusGallenteEngineering"),
                           skill="Gallente Engineering Systems")
