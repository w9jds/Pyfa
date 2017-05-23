# subSystemBonusCaldariElectronicScanProbeStrength
#
# Used by:
# Subsystem: Tengu Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength", module.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                                    skill="Caldari Electronic Systems")
