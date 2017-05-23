# eliteBonusGunshipProjectileFalloff2
#
# Used by:
# Ship: Wolf
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "falloff", ship.getModifiedItemAttr("eliteBonusGunship2"), skill="Assault Frigates")
