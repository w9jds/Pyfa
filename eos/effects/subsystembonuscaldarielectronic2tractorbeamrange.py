# subSystemBonusCaldariElectronic2TractorBeamRange
#
# Used by:
# Subsystem: Tengu Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusCaldariElectronic2"),
                                  skill="Caldari Electronic Systems")
