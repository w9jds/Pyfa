# shipNeutDestabilizationAmountBonusRookie
#
# Used by:
# Ship: Hematos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Neutralizer",
                                  "energyNeutralizerAmount", ship.getModifiedItemAttr("rookieNeutDrain"))
