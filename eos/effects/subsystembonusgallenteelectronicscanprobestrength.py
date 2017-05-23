# subSystemBonusGallenteElectronicScanProbeStrength
#
# Used by:
# Subsystem: Proteus Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength",
                                    module.getModifiedItemAttr("subsystemBonusGallenteElectronic"),
                                    skill="Gallente Electronic Systems")
