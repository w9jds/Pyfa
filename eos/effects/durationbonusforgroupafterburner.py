# durationBonusForGroupAfterburner
#
# Used by:
# Modules named like: Engine Thermal Shielding (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "duration", container.getModifiedItemAttr("durationBonus"))
