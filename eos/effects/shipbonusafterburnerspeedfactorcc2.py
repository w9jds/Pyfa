# shipBonusAfterburnerSpeedFactorCC2
#
# Used by:
# Ship: Fiend
# Ship: Phantasm
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "speedFactor", container.getModifiedItemAttr("shipBonusCC2"), skill="Caldari Cruiser")
