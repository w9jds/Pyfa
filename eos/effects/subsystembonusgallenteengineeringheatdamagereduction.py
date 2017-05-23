# subsystemBonusGallenteEngineeringHeatDamageReduction
#
# Used by:
# Subsystem: Proteus Engineering - Supplemental Coolant Injector
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  module.getModifiedItemAttr("subsystemBonusGallenteEngineering"),
                                  skill="Gallente Engineering Systems")
