# drawbackPowerNeedLasers
#
# Used by:
# Modules from group: Rig Energy Weapon (56 of 56)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "power", container.getModifiedItemAttr("drawback"))
