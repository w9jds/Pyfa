# subSystemBonusMinmatarElectronicScanProbeStrength
#
# Used by:
# Subsystem: Loki Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength",
                                    container.getModifiedItemAttr("subsystemBonusMinmatarElectronic"),
                                    skill="Minmatar Electronic Systems")
