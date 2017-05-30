# subSystemBonusAmarrElectronicScanProbeStrength
#
# Used by:
# Subsystem: Legion Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength", container.getModifiedItemAttr("subsystemBonusAmarrElectronic"),
                                    skill="Amarr Electronic Systems")
