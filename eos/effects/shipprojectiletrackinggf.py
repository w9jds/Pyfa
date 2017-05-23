# shipProjectileTrackingGF
#
# Used by:
# Ship: Chremoas
# Ship: Dramiel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("shipBonusGF"), skill="Gallente Frigate")
