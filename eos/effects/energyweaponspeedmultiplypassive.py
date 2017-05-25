# energyWeaponSpeedMultiplyPassive
#
# Used by:
# Modules named like: Energy Burst Aerator (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Energy Weapon",
                                     "speed", container.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties=True)
