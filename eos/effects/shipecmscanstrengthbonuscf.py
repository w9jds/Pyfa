# shipECMScanStrengthBonusCF
#
# Used by:
# Variations of ship: Griffin (3 of 3)
effectType = "passive"


def handler(fit, ship, context):
    for sensor_type in ("Gravimetric", "Ladar", "Radar", "Magnetometric"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                      "scan{0}StrengthBonus".format(sensor_type),
                                      ship.getModifiedItemAttr("shipBonusCF"), skill="Caldari Frigate")
