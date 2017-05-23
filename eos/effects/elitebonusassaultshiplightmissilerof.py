# eliteBonusAssaultShipLightMissileROF
#
# Used by:
# Ship: Cambion
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Light",
                                  "speed", ship.getModifiedItemAttr("eliteBonusGunship1"), skill="Assault Frigates")
