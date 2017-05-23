# subsystemBonusGallentePropulsionABMWDCapNeed
#
# Used by:
# Subsystem: Proteus Propulsion - Localized Injectors
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "capacitorNeed", module.getModifiedItemAttr("subsystemBonusGallentePropulsion"),
                                  skill="Gallente Propulsion Systems")
