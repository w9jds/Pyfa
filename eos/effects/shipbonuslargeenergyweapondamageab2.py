# shipBonusLargeEnergyWeaponDamageAB2
#
# Used by:
# Ship: Abaddon
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusAB2"),
                                  skill="Amarr Battleship")
