# shipRocketRoFBonusAF2
#
# Used by:
# Ship: Malediction
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Rocket",
                                  "speed", ship.getModifiedItemAttr("shipBonus2AF"), skill="Amarr Frigate")
