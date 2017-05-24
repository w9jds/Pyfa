# subsystemBonusCaldariElectronicCPU
#
# Used by:
# Subsystem: Tengu Electronics - CPU Efficiency Gate
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("cpuOutput", container.getModifiedItemAttr("subsystemBonusCaldariElectronic"),
                           skill="Caldari Electronic Systems")
