# subSystemBonusGallenteElectronic2TractorBeamRange
#
# Used by:
# Subsystem: Proteus Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusGallenteElectronic2"),
                                  skill="Gallente Electronic Systems")
