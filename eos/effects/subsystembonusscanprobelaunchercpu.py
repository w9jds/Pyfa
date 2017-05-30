# subsystemBonusScanProbeLauncherCPU
#
# Used by:
# Subsystems named like: Electronics Emergent Locus Analyzer (4 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Scan Probe Launcher",
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus"))
