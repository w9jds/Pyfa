# subSystemBonusAmarrElectronic2TractorBeamRange
#
# Used by:
# Subsystem: Legion Electronics - Emergent Locus Analyzer
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusAmarrElectronic2"),
                                  skill="Amarr Electronic Systems")
