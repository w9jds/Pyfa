# shipBonusNoctisSalvageCycle
#
# Used by:
# Ship: Noctis
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Salvaging"),
                                  "duration", ship.getModifiedItemAttr("shipBonusOreIndustrial1"),
                                  skill="ORE Industrial")
