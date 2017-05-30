# shipSHTRoFGallenteTacticalDestroyer1
#
# Used by:
# Ship: Hecate
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusTacticalDestroyerGallente1"),
                                  skill="Gallente Tactical Destroyer")
