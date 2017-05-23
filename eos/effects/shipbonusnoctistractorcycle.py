# shipBonusNoctisTractorCycle
#
# Used by:
# Ship: Noctis
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "duration", ship.getModifiedItemAttr("shipBonusOreIndustrial1"),
                                  skill="ORE Industrial")
