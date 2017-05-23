# shipBonusSmallEnergyTurretTracking2AF
#
# Used by:
# Ship: Imp
# Ship: Succubus
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("shipBonus2AF"), skill="Amarr Frigate")
