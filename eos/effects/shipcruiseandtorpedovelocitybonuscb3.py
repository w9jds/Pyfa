# shipCruiseAndTorpedoVelocityBonusCB3
#
# Used by:
# Ship: Golem
# Ship: Widow
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(
            lambda mod: mod.charge.requiresSkill("Cruise Missiles") or mod.charge.requiresSkill("Torpedoes"),
            "maxVelocity", ship.getModifiedItemAttr("shipBonusCB3"), skill="Caldari Battleship")
