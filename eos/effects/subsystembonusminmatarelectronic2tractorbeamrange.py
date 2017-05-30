# subSystemBonusMinmatarElectronic2TractorBeamRange
#
# Used by:
# Subsystem: Loki Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusMinmatarElectronic2"),
                                  skill="Minmatar Electronic Systems")
