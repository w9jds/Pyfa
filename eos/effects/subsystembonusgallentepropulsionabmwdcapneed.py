# subsystemBonusGallentePropulsionABMWDCapNeed
#
# Used by:
# Subsystem: Proteus Propulsion - Localized Injectors
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "capacitorNeed", container.getModifiedItemAttr("subsystemBonusGallentePropulsion"),
                                  skill="Gallente Propulsion Systems")
