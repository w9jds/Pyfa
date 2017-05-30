# subSystemBonusCaldariElectronicScanProbeStrength
#
# Used by:
# Subsystem: Tengu Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength", container.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                                    skill="Caldari Electronic Systems")
