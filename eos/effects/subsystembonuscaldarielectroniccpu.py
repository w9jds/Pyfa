# subsystemBonusCaldariElectronicCPU
#
# Used by:
# Subsystem: Tengu Electronics - CPU Efficiency Gate
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                           skill="Caldari Electronic Systems")
