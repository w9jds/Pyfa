# subsystemBonusGallenteElectronicCPU
#
# Used by:
# Subsystem: Proteus Electronics - CPU Efficiency Gate
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("subsystemBonusGallenteElectronic"),
                           skill="Gallente Electronic Systems")
