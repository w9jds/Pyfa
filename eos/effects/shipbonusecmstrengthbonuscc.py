# shipBonusECMStrengthBonusCC
#
# Used by:
# Ship: Blackbird
effectType = "passive"


def handler(fit, ship, context):
    for sensor_type in ("Gravimetric", "Magnetometric", "Ladar", "Radar"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                      "scan{0}StrengthBonus".format(sensor_type), ship.getModifiedItemAttr("shipBonusCC"),
                                      skill="Caldari Cruiser")
