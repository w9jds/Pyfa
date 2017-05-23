# shipDroneScoutThermalDamageGF2
#
# Used by:
# Ship: Helios
effectType = "passive"


def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda mod: mod.item.requiresSkill("Drone Avionics"),
                                 "thermalDamage", ship.getModifiedItemAttr("shipBonusGF2"), skill="Gallente Frigate")
