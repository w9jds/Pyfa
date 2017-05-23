# shipBonusMediumDroneArmorHPPirateFaction
#
# Used by:
# Ship: Chameleon
# Ship: Gila
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Medium Drone Operation"),
                                 "armorHP", ship.getModifiedItemAttr("shipBonusRole7"))
