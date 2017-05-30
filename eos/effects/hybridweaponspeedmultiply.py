# hybridWeaponSpeedMultiply
#
# Used by:
# Modules from group: Magnetic Field Stabilizer (14 of 14)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                     "speed", container.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties=True)
