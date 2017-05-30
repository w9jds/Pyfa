# shipHybridDmgPirateBattleship
#
# Used by:
# Ship: Vindicator
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusRole7"))
