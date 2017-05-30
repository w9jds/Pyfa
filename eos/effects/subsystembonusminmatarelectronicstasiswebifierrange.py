# subsystemBonusMinmatarElectronicStasisWebifierRange
#
# Used by:
# Subsystem: Loki Electronics - Immobility Drivers
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusMinmatarElectronic"),
                                  skill="Minmatar Electronic Systems")
