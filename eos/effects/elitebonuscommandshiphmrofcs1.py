# eliteBonusCommandShipHMRoFCS1
#
# Used by:
# Ship: Claymore
# Ship: Nighthawk
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy",
                                  "speed", ship.getModifiedItemAttr("eliteBonusCommandShips1"), skill="Command Ships")
