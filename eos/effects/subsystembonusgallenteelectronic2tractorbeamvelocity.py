# subSystemBonusGallenteElectronic2TractorBeamVelocity
#
# Used by:
# Subsystem: Proteus Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxTractorVelocity", container.getModifiedItemAttr("subsystemBonusGallenteElectronic2"),
                                  skill="Gallente Electronic Systems")
