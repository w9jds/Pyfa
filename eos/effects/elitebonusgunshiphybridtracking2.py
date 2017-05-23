# eliteBonusGunshipHybridTracking2
#
# Used by:
# Ship: Enyo
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("eliteBonusGunship2"),
                                  skill="Assault Frigates")
