# subsystemBonusGallenteElectronicWarpScrambleRange
#
# Used by:
# Subsystem: Proteus Electronics - Friction Extension Processor
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Warp Scrambler",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusGallenteElectronic"),
                                  skill="Gallente Electronic Systems")
