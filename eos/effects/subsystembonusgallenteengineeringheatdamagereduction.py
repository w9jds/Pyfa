# subsystemBonusGallenteEngineeringHeatDamageReduction
#
# Used by:
# Subsystem: Proteus Engineering - Supplemental Coolant Injector
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  container.getModifiedItemAttr("subsystemBonusGallenteEngineering"),
                                  skill="Gallente Engineering Systems")
