# shipBonusAfterburnerSpeedFactorCF2
#
# Used by:
# Ship: Imp
# Ship: Succubus
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "speedFactor", container.getModifiedItemAttr("shipBonusCF2"), skill="Caldari Frigate")
