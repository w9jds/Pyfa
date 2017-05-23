# eliteBonusViolatorsLargeHybridTurretTracking1
#
# Used by:
# Ship: Kronos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("eliteBonusViolators1"), skill="Marauders")
