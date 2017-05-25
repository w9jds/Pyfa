# hybridWeaponDamageMultiplyPassive
#
# Used by:
# Modules named like: Hybrid Collision Accelerator (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                     "damageMultiplier", container.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties=True)
