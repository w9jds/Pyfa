# shipMissileRoFCaldariTacticalDestroyer1
#
# Used by:
# Ship: Jackdaw
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                  "speed", ship.getModifiedItemAttr("shipBonusTacticalDestroyerCaldari1"),
                                  skill="Caldari Tactical Destroyer")
