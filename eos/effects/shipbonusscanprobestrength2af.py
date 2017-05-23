# shipBonusScanProbeStrength2AF
#
# Used by:
# Ship: Magnate
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength", ship.getModifiedItemAttr("shipBonus2AF"),
                                    skill="Amarr Frigate")
