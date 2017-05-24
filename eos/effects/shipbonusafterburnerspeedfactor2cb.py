# shipBonusAfterburnerSpeedFactor2CB
#
# Used by:
# Ship: Nightmare
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "speedFactor", container.getModifiedItemAttr("shipBonus2CB"), skill="Caldari Battleship")
