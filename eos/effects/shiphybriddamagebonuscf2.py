# shipHybridDamageBonusCF2
#
# Used by:
# Ship: Griffin Navy Issue
# Ship: Merlin
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusCF2"), skill="Caldari Frigate")
