# subsystemBonusGallenteElectronicCPU
#
# Used by:
# Subsystem: Proteus Electronics - CPU Efficiency Gate
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("cpuOutput", container.getModifiedItemAttr("subsystemBonusGallenteElectronic"),
                           skill="Gallente Electronic Systems")
