# shipBonusLightDroneHPPirateFaction
#
# Used by:
# Ship: Whiptail
# Ship: Worm
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Light Drone Operation"),
                                 "hp", ship.getModifiedItemAttr("shipBonusRole7"))
