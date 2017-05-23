# dataminerModuleDurationReduction
#
# Used by:
# Implant: Poteque 'Prospector' Environmental Analysis EY-1005
effectType = "passive"


def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Data Miners",
                                  "duration", implant.getModifiedItemAttr("durationBonus"))
