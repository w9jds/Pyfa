# subsystemBonusAmarrEngineeringHeatDamageReduction
#
# Used by:
# Subsystem: Legion Engineering - Supplemental Coolant Injector
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  container.getModifiedItemAttr("subsystemBonusAmarrEngineering"),
                                  skill="Amarr Engineering Systems")
