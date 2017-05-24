# subsystemBonusMinmatarEngineeringHeatDamageReduction
#
# Used by:
# Subsystem: Loki Engineering - Supplemental Coolant Injector
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  container.getModifiedItemAttr("subsystemBonusMinmatarEngineering"),
                                  skill="Minmatar Engineering Systems")
