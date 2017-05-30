# subsystemBonusAmarrElectronicEnergyDestabilizerAmount
#
# Used by:
# Subsystem: Legion Electronics - Energy Parasitic Complex
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Neutralizer",
                                  "energyNeutralizerAmount",
                                  container.getModifiedItemAttr("subsystemBonusAmarrElectronic"),
                                  skill="Amarr Electronic Systems")
